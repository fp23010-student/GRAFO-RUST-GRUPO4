// ============================================================
// MÓDULO: algoritmos.rs
// RESPONSABLE: Jose Luis Rosales Moran
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

/// Encuentra la ruta más corta (en número de saltos) desde
/// `inicio` hasta `destino`.
/// Devuelve Some(Vec de índices que forman la ruta) o None
/// si no existe camino entre los dos nodos.
///
/// Pistas:
///   1. Usa una cola (VecDeque) para procesar nodos nivel por nivel.
///   2. Lleva un Vec<bool> de visitados para no repetir nodos.
///   3. Lleva un Vec<Option<usize>> de "padres" para reconstruir la ruta al final.
pub fn bfs_ruta_corta(grafo: &Grafo, inicio: usize, destino: usize) -> Option<Vec<usize>> {
    if inicio == destino {
        return Some(vec![inicio]);
    }

    let n = grafo.num_nodos();
    let mut visitado = vec![false; n];
    let mut padre: Vec<Option<usize>> = vec![None; n];
    let mut cola: VecDeque<usize> = VecDeque::new();

    visitado[inicio] = true;
    cola.push_back(inicio);

    while let Some(actual) = cola.pop_front() {
        for &vecino in grafo.vecinos(actual) {
            if !visitado[vecino] {
                visitado[vecino] = true;
                padre[vecino] = Some(actual);
                cola.push_back(vecino);

                if vecino == destino {
                    // Reconstruir la ruta
                    let mut ruta = Vec::new();
                    let mut actual = destino;
                    while let Some(p) = padre[actual] {
                        ruta.push(actual);
                        actual = p;
                    }
                    ruta.push(inicio);
                    ruta.reverse();
                    return Some(ruta);
                }
            }
        }
    }

    None // No hay camino
}

// ─────────────────────────────────────────────
// DFS — Búsqueda en Profundidad
// ─────────────────────────────────────────────

/// Detecta si el grafo contiene algún ciclo.
/// Retorna true si existe al menos un ciclo, false si no.
pub fn dfs_detectar_ciclo(grafo: &Grafo) -> bool {
    let n = grafo.num_nodos();
    let mut visitado = vec![false; n];

    for i in 0..n {
        if !visitado[i] {
            if dfs_auxiliar(grafo, i, None, &mut visitado) {
                return true;
            }
        }
    }
    false
}

/// Función auxiliar recursiva para el DFS.
/// `padre` es el nodo desde donde llegamos (para no contar
/// la arista de vuelta como ciclo).
fn dfs_auxiliar(
    grafo: &Grafo,
    nodo: usize,
    padre: Option<usize>,
    visitado: &mut Vec<bool>,
) -> bool {
    visitado[nodo] = true;

    for &vecino in grafo.vecinos(nodo) {
        if !visitado[vecino] {
            // Explorar recursivamente
            if dfs_auxiliar(grafo, vecino, Some(nodo), visitado) {
                return true;
            }
        } else if Some(vecino) != padre {
            // Encontramos un back-edge → ciclo
            return true;
        }
    }
    false
}
