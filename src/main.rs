// ============================================================
// MÓDULO: main.rs
// RESPONSABLE: Integrante 1 — [PON TU NOMBRE AQUÍ]
//
// TODO: Conecta todos los módulos y muestra los resultados.
//       Este archivo es el director de orquesta: usa lo que
//       construyeron tus compañeros para armar y consultar el grafo.
// ============================================================

mod grafo;
mod modelo;
mod algoritmos;

use grafo::Grafo;
use modelo::{usuarios, amistades};
use algoritmos::{bfs_ruta_corta, dfs_detectar_ciclo};

fn main() {
    println!("=== RED SOCIAL — GRAFO-RUST-GRUPO4 ===\n");

    // TODO 1: Cargar los usuarios y amistades desde modelo.rs
    let usuarios  = usuarios();
    let amistades = amistades();

    // TODO 2: Extraer solo los nombres en un Vec<String> para
    //         pasárselos a grafo.imprimir()
    let nombres: Vec<String> = todo!("Extraer nombres de cada usuario");

    // TODO 3: Crear el grafo con el número correcto de nodos
    //         y agregar todas las aristas
    let mut red = todo!("Crear Grafo::nuevo(...) con la cantidad de usuarios");
    for (a, b) in &amistades {
        todo!("Llamar a red.agregar_arista con cada par de amigos");
    }

    // TODO 4: Imprimir la lista de adyacencia completa
    todo!("Llamar a red.imprimir(&nombres)");

    // TODO 5: Usar BFS para encontrar la ruta más corta entre
    //         dos usuarios de tu elección (por índice)
    let origen  = 0; // TODO: cambia al índice que quieras
    let destino = 0; // TODO: cambia al índice que quieras
    println!("\nBFS: ruta más corta de {} a {}:", nombres[origen], nombres[destino]);
    match bfs_ruta_corta(&red, origen, destino) {
        Some(ruta) => {
            // TODO: imprime la ruta con nombres, no con índices
            todo!("Imprimir la ruta como nombres separados por →")
        }
        None => println!("No existe camino entre esos usuarios."),
    }

    // TODO 6: Usar DFS para detectar si hay ciclos en la red
    println!("\nDFS: detección de ciclos...");
    todo!("Llamar a dfs_detectar_ciclo e imprimir si hay ciclo o no");
}
