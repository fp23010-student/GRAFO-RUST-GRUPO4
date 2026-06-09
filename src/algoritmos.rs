// ============================================================
// MÓDULO: algoritmos.rs
// RESPONSABLE: Integrante 3 — [PON TU NOMBRE AQUÍ]
//
// TODO: Implementa los dos algoritmos de recorrido.
//
// REQUISITO MÍNIMO (elige uno para la exposición):
//   - BFS: encontrar la ruta con menos conexiones entre dos usuarios
//   - DFS: detectar si existen ciclos en la red
//
// RETO EXTRA (para nota máxima):
//   Implementa ambos.
// ============================================================

use std::collections::VecDeque; // útil para la cola del BFS
use crate::grafo::Grafo;

// ─────────────────────────────────────────────
// BFS — Búsqueda en Anchura
// ─────────────────────────────────────────────

/// TODO: Encuentra la ruta más corta (en número de saltos) desde
///       `inicio` hasta `destino`.
///       Devuelve Some(Vec de índices que forman la ruta) o None
///       si no existe camino entre los dos nodos.
///
/// Pistas:
///   1. Usa una cola (VecDeque) para procesar nodos nivel por nivel.
///   2. Lleva un Vec<bool> de visitados para no repetir nodos.
///   3. Lleva un Vec<Option<usize>> de "padres" para reconstruir la ruta al final.
pub fn bfs_ruta_corta(grafo: &Grafo, inicio: usize, destino: usize) -> Option<Vec<usize>> {
    todo!("Implementar BFS para encontrar ruta más corta")
}

// ─────────────────────────────────────────────
// DFS — Búsqueda en Profundidad
// ─────────────────────────────────────────────

/// TODO: Detecta si el grafo contiene algún ciclo.
///       Retorna true si existe al menos un ciclo, false si no.
///
/// Pistas:
///   1. Recorre cada nodo no visitado llamando a una función auxiliar recursiva.
///   2. En la función auxiliar, si llegas a un nodo ya visitado que NO es
///      tu padre inmediato → encontraste un ciclo.
pub fn dfs_detectar_ciclo(grafo: &Grafo) -> bool {
    todo!("Implementar DFS para detectar ciclos")
}

/// TODO: Función auxiliar recursiva para el DFS.
///       `padre` es el nodo desde donde llegamos (para no contar
///       la arista de vuelta como ciclo).
fn dfs_auxiliar(
    grafo: &Grafo,
    nodo: usize,
    padre: Option<usize>,
    visitado: &mut Vec<bool>,
) -> bool {
    todo!("Implementar recursión del DFS")
}
