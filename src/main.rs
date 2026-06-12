// ============================================================
// MÓDULO: main.rs
// RESPONSABLE: Cristian Guillen
//
// TODO: Conecta todos los módulos y muestra los resultados.
//       Conecta todos los módulos y muestra los resultados.
// ============================================================
 
mod grafo;
mod modelo;
mod algoritmos;

use grafo::Grafo;
use modelo::{usuarios, amistades};
use algoritmos::{bfs_ruta_corta, dfs_detectar_ciclo};

fn main() {
    println!("=== RED SOCIAL — GRAFO-RUST-GRUPO4 ===\n");

    // 1: Cargar los usuarios y amistades desde modelo.rs
    let usuarios  = usuarios();
    let amistades = amistades();

    // 2: Extraer solo los nombres en un Vec<String>
    let nombres: Vec<String> = usuarios.iter().map(|u| u.nombre.clone()).collect();

    // 3: Crear el grafo y agregar todas las aristas
    let mut red = Grafo::nuevo(usuarios.len());
    for (a, b) in &amistades {
        red.agregar_arista(*a, *b);
    }

    // 4: Imprimir la lista de adyacencia completa
    red.imprimir(&nombres);
    
    println!("=== INFORMACIÓN DE USUARIOS ===\n");
    for (i, u) in usuarios.iter().enumerate() {
        println!("  [{}] {} | Edad: {} | Carrera: {}", i, u.nombre, u.edad, u.carrera);
    }
    println!();

    // 5: BFS — ruta más corta entre Hamilton (0) y Carlos (9)
    let origen  = 0; // Hamilton Figueroa
    let destino = 9; // Carlos Mendez
    println!("BFS: ruta más corta de {} a {}:", nombres[origen], nombres[destino]);
    match bfs_ruta_corta(&red, origen, destino) {
        Some(ruta) => {
            let ruta_nombres: Vec<&str> = ruta.iter().map(|&i| nombres[i].as_str()).collect();
            println!("{}", ruta_nombres.join(" → "));
        }
        None => println!("No existe camino entre esos usuarios."),
    }

    // 6: DFS — detectar si hay ciclos en la red
    println!("\nDFS: detección de ciclos...");
    if dfs_detectar_ciclo(&red) {
        println!(" Se detectó al menos un ciclo en la red social.");
    } else {
        println!(" No se encontraron ciclos en la red social.");
    }
}