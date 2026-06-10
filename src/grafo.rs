// ============================================================
// MÓDULO: grafo.rs
// RESPONSABLE: Mynor Cabrera
//
// Implementa la estructura Grafo usando lista de adyacencia
// basada en índices Vec<usize>.
//
// PREGUNTA CLAVE para la exposición:
//   ¿Por qué usamos índices usize en vez de referencias &Nodo?
// ============================================================

/// Estructura principal del grafo.
/// Internamente usa una lista de adyacencia:
///   adyacencia[i] = Vec con los índices de los vecinos del nodo i
pub struct Grafo {
    /// Número total de nodos en el grafo
    num_nodos: usize,
    /// Lista de adyacencia: cada posición contiene los vecinos de ese nodo
    adyacencia: Vec<Vec<usize>>,
}

impl Grafo {
    ///Crea un grafo vacío con `n` nodos y sin aristas.
    pub fn nuevo(n: usize) -> Self {
        Grafo {
            num_nodos: n,
            // Creamos n listas vacías, una por cada nodo
            adyacencia: vec![Vec::new(); n],
        }
    }

    /// Agrega una arista BIDIRECCIONAL entre los nodos `a` y `b`.
    /// Si A es amigo de B, entonces B también es amigo de A.
    pub fn agregar_arista(&mut self, a: usize, b: usize) {
        self.adyacencia[a].push(b);
        self.adyacencia[b].push(a);
    }

    /// Devuelve una referencia a la lista de vecinos del nodo `nodo`.
    pub fn vecinos(&self, nodo: usize) -> &Vec<usize> {
        &self.adyacencia[nodo]
    }

    /// Devuelve el número de nodos del grafo.
    pub fn num_nodos(&self) -> usize {
        self.num_nodos
    }

    /// Imprime la lista de adyacencia completa con nombres en vez de índices.
    /// Ejemplo de salida:
    ///   Hamilton Figueroa → [Mynor Cabrera, Cristian Guillen, ...]
    ///   Mynor Cabrera     → [Hamilton Figueroa, Cristian Guillen, ...]
    pub fn imprimir(&self, nombres: &[String]) {
        println!("=== LISTA DE ADYACENCIA (Red Social) ===\n");
        for i in 0..self.num_nodos {
            // Convertimos los índices de vecinos a nombres
            let vecinos_nombres: Vec<&str> = self.adyacencia[i]
                .iter()
                .map(|&idx| nombres[idx].as_str())
                .collect();
            println!("{:<25} → {:?}", nombres[i], vecinos_nombres);
        }
        println!();
    }
}