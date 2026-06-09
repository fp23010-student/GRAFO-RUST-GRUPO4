// ============================================================
// MÓDULO: modelo.rs
// RESPONSABLE: Integrante 4 — [PON TU NOMBRE AQUÍ]
//
// TODO: Define los datos del mundo real.
//       Debes crear los usuarios de la red social y
//       las amistades entre ellos.
// ============================================================

/// TODO: Define los campos que debe tener un Usuario
///       (mínimo: nombre, edad, y algún campo extra de tu elección)
#[derive(Debug, Clone)]
pub struct Usuario {
    // TODO: agrega los campos aquí
}

impl Usuario {
    /// TODO: implementa el constructor
    pub fn nuevo(/* TODO: parámetros */) -> Self {
        todo!("Implementar constructor de Usuario")
    }
}

/// TODO: Devuelve un Vec con al menos 6 usuarios inventados por tu equipo.
///       Cada usuario se identificará por su índice en este Vec (0, 1, 2...).
pub fn usuarios() -> Vec<Usuario> {
    todo!("Crear la lista de usuarios de la red social")
}

/// TODO: Devuelve las amistades como pares de índices (a, b).
///       Deben existir al menos 8 amistades para que el grafo
///       sea interesante y tenga ciclos.
///       Ejemplo: (0, 1) significa que el usuario 0 es amigo del usuario 1.
pub fn amistades() -> Vec<(usize, usize)> {
    todo!("Definir las amistades entre usuarios usando sus índices")
}
