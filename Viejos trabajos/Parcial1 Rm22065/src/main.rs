use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader, Write};
use std::process::{Command, Stdio};

#[derive(Debug, Eq, PartialEq, Hash)]
struct ErrorCritico {
    id_error: u32,
    mensaje: String,
}
fn main() {
    let carnet = "RM22065";
    let archivo_salida = format!("alertas_{}.dat", carnet.to_lowercase());

    let mut proceso = Command::new("./generador_logs")
        .stdout(Stdio::piped())
        .spawn()
        .expect("No se pudo ejecutar el generador de logs");

    let stdout = proceso.stdout.take().expect("No se pudo capturar stdout");
    let reader = BufReader::new(stdout);

    let mut errores_unicos: HashSet<ErrorCritico> = HashSet::new();

    for linea in reader.lines() {
        if let Ok(linea) = linea {
            if linea.contains("CRITICAL_ERR") {
                if let Some(error) = parsear_error(&linea) {
                    errores_unicos.insert(error);
                }
            }
        }
    }
    let codigo_busqueda = "401";
    let mut resultado_busqueda: Option<String> = None;
    for error in &errores_unicos {
        if error.mensaje.contains(codigo_busqueda) {
            if let Some(descripcion) = extraer_descripcion(&error.mensaje) {
                resultado_busqueda = Some(descripcion);
                break;
            }
        }
    }
    let resultado_final = match resultado_busqueda {
        Some(desc) => desc,
        None => panic!("No se encontró el error con código {}", codigo_busqueda),
    };
    let mut archivo = File::create(&archivo_salida)
        .expect("No se pudo crear el archivo de salida");

    writeln!(archivo, "Carnet: {}", carnet).unwrap();

    for error in &errores_unicos {
        writeln!(
            archivo,
            "id_error: {} : {}",
            error.id_error, error.mensaje
        )
        .unwrap();
    }

    writeln!(
        archivo,
        "Error crítico encontrado:  mensaje: {}",
        resultado_final
    )
    .unwrap();
}
fn parsear_error(linea: &str) -> Option<ErrorCritico> {
    let partes: Vec<&str> = linea.split("id_error:").collect();
    if partes.len() < 2 {
        return None;
    }

    let resto = partes[1].trim();

    let partes2: Vec<&str> = resto.split(":").collect();
    if partes2.len() < 2 {
        return None;
    }

    let id_error = partes2[0].trim().parse::<u32>().ok()?;

    let mensaje_index = linea.find("CRITICAL_ERR")?;
    let mensaje = linea[mensaje_index..].to_string();

    Some(ErrorCritico { id_error, mensaje })
}
fn extraer_descripcion(mensaje: &str) -> Option<String> {
    let partes: Vec<&str> = mensaje.split(',').collect();
    if partes.len() < 2 {
        return None;
    }
    Some(partes[1].trim().to_string())
}