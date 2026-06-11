// ============================================================
// MÓDULO: modelo.rs
// RESPONSABLE: Hamilton Figueroa
//
// Define los datos del mundo real: los usuarios de la red social
// y las amistades entre ellos.
// ============================================================

/// Representa a un usuario de la red social.
#[derive(Debug, Clone)]
pub struct Usuario {
    pub nombre: String,
    pub edad: u8,
    pub carrera: String,
}

impl Usuario {
    pub fn nuevo(nombre: &str, edad: u8, carrera: &str) -> Self {
        Usuario {
            nombre: nombre.to_string(),
            edad,
            carrera: carrera.to_string(),
        }
    }
}

/// Lista de usuarios de la red social.
/// El índice de cada usuario en este Vec es su ID en el grafo.
pub fn usuarios() -> Vec<Usuario> {
    vec![
        // índice 0
        Usuario::nuevo("Hamilton Figueroa", 20, "Ingeniería en Sistemas"),
        // índice 1
        Usuario::nuevo("Mynor Cabrera",     21, "Ingeniería en Sistemas"),
        // índice 2
        Usuario::nuevo("Cristian Guillen",  20, "Ingeniería en Sistemas"),
        // índice 3
        Usuario::nuevo("Jose Rosales",      22, "Ingeniería en Sistemas"),
        // índice 4
        Usuario::nuevo("Sofia Hernandez",   21, "Ingeniería Civil"),
        // índice 5
        Usuario::nuevo("Diego Ramirez",     23, "Administración de Empresas"),
        // índice 6
        Usuario::nuevo("Valeria Torres",    20, "Diseño Gráfico"),
        // índice 7
        Usuario::nuevo("Luis Morales",      24, "Ingeniería en Sistemas"),
        // índice 8
        Usuario::nuevo("Andrea Perez",      21, "Psicología"),
        // índice 9
        Usuario::nuevo("Carlos Mendez",     22, "Ingeniería Civil"),
    ]
}

/// Lista de amistades como pares de índices (a, b).
/// Como la amistad es bidireccional, grafo.rs se encarga
/// de agregarla en ambas direcciones.
pub fn amistades() -> Vec<(usize, usize)> {
    vec![
        // El grupo principal (los 4 integrantes se conocen entre sí)
        (0, 1), // Hamilton  <-> Mynor
        (0, 2), // Hamilton  <-> Cristian
        (0, 3), // Hamilton  <-> Jose
        (1, 2), // Mynor     <-> Cristian
        (1, 3), // Mynor     <-> Jose
        (2, 3), // Cristian  <-> Jose

        // Conexiones con compañeros de la U
        (0, 4), // Hamilton  <-> Sofia
        (0, 7), // Hamilton  <-> Luis
        (1, 5), // Mynor     <-> Diego
        (1, 8), // Mynor     <-> Andrea
        (2, 6), // Cristian  <-> Valeria
        (2, 9), // Cristian  <-> Carlos
        (3, 5), // Jose      <-> Diego
        (3, 9), // Jose      <-> Carlos

        // Conexiones entre conocidos
        (4, 6), // Sofia     <-> Valeria
        (5, 7), // Diego     <-> Luis
        (6, 8), // Valeria   <-> Andrea
        (7, 9), // Luis      <-> Carlos
        (8, 9), // Andrea    <-> Carlos
        (4, 9), // Sofia     <-> Carlos
    ]
}