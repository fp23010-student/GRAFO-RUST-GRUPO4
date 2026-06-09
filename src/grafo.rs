// ============================================================
// MÓDULO: grafo.rs
// RESPONSABLE: Integrante 2 — [PON TU NOMBRE AQUÍ]
//
// TODO: Implementa la estructura Grafo usando lista de adyacencia
//       basada en índices Vec<usize>.
//
// PREGUNTA CLAVE que debes poder responder en la exposición:
//   ¿Por qué usamos índices usize en vez de referencias &Nodo?
//   Pista: investiga "Rust ownership cycles" y "borrow checker"
// ============================================================

/// TODO: Define la estructura Grafo.
///       Debe contener:
///         - El número de nodos
///         - La lista de adyacencia (Vec de Vecs de índices)
pub struct Grafo {
    // TODO: agrega los campos aquí
}

impl Grafo {
    /// TODO: Crea un grafo vacío con `n` nodos.
    pub fn nuevo(n: usize) -> Self {
        todo!("Crear grafo con n nodos vacíos")
    }

    /// TODO: Agrega una arista BIDIRECCIONAL entre los nodos `a` y `b`.
    ///       Recuerda: si A es amigo de B, entonces B también es amigo de A.
    pub fn agregar_arista(&mut self, a: usize, b: usize) {
        todo!("Agregar arista en ambas direcciones")
    }

    /// TODO: Devuelve una referencia a los vecinos del nodo `nodo`.
    pub fn vecinos(&self, nodo: usize) -> &Vec<usize> {
        todo!("Retornar vecinos del nodo")
    }

    /// TODO: Imprime la lista de adyacencia de forma legible.
    ///       Usa el Vec de nombres para mostrar nombres en vez de índices.
    ///       Ejemplo de salida esperada:
    ///         Ana    → [Bruno, Carla]
    ///         Bruno  → [Ana, Diego]
    pub fn imprimir(&self, nombres: &[String]) {
        todo!("Imprimir lista de adyacencia con nombres")
    }
}
