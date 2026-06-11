# 🕸️ GRAFO-RUST-GRUPO4

Red social de amigos modelada como grafo no dirigido en Rust.

---

## 📁 Estructura del Proyecto

```
GRAFO-RUST-GRUPO4/
├── Cargo.toml
├── .gitignore
├── README.md
└── src/
    ├── main.rs         → Integrante 1
    ├── grafo.rs        → Integrante 2
    ├── algoritmos.rs   → Integrante 3
    └── modelo.rs       → Integrante 4
```

---

## 👥 ¿Quién hace qué?

| Archivo | Integrante | Tarea |
|---|---|---|
| `main.rs` | Integrante 1 | Conectar todo: construir el grafo y mostrar resultados |
| `grafo.rs` | Integrante 2 | Implementar la struct `Grafo` con lista de adyacencia |
| `algoritmos.rs` | Integrante 3 | Implementar BFS y DFS |
| `modelo.rs` | Integrante 4 | Definir usuarios y amistades |

Cada archivo tiene comentarios `// TODO:` que explican exactamente qué implementar.

---

## 🚀 Cómo correr el proyecto

```bash
# Requiere Rust instalado: https://rustup.rs/
cargo run
```

---

## ⚠️ Reglas del equipo

1. **No modifiques el archivo de otro** sin avisarle.
2. Cada uno debe poder **explicar su propio código** en la exposición.
3. El programa debe **compilar sin errores** (`cargo build`) antes de la entrega.
4. Prohibido dejar `todo!()` sin implementar en la entrega final.

---

## 📚 Recursos útiles

- [The Rust Book (español)](https://rustlang-es.org/the-rust-book/)  
- [Rust by Example — Ownership](https://doc.rust-lang.org/rust-by-example/scope/ownership.html)  
- [petgraph docs](https://docs.rs/petgraph)  
- [Visualizador de BFS/DFS](https://visualgo.net/en/bfs)
