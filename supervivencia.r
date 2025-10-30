set.seed(123)

simular_paletas_unicas <- function() {
  # Crear 9 estudiantes con contadores de dulces A, B, C y paletas P
  estudiantes <- vector("list", 9)
  for (i in 1:9) estudiantes[[i]] <- c(A=0, B=0, C=0, P=0)
  
  iteraciones <- 0
  contador_paleta <- 1
  
  cat("INICIO DE LA SIMULACION DE DULCES Y PALETAS (1 paleta por estudiante)\n")
  
  while (TRUE) {
    iteraciones <- iteraciones + 1
    cat("\nIteracion", iteraciones, "\n")
    
    # 1. Repartir 2 dulces aleatorios a cada estudiante
    for (i in 1:9) {
      nuevos <- sample(c("A", "B", "C"), 2, replace = TRUE)
      for (candy in nuevos) estudiantes[[i]][candy] <- estudiantes[[i]][candy] + 1
    }
    
    # 2. Canjes y devoluciones
    for (i in 1:9) {
      # Solo estudiantes sin paleta pueden intentar canjear
      if (estudiantes[[i]]["P"] == 0) {
        sets <- min(estudiantes[[i]][c("A", "B", "C")])
        
        if (sets >= 2) {
          # Canje por 6 dulces (2 sets) -> 1 paleta + 1 dulce al azar
          estudiantes[[i]]["P"] <- 1
          estudiantes[[i]][c("A","B","C")] <- estudiantes[[i]][c("A","B","C")] - 2
          bonus <- sample(c("A", "B", "C"), 1)
          estudiantes[[i]][bonus] <- estudiantes[[i]][bonus] + 1
          cat(sprintf("  Paleta #%d -> Estudiante %d (2 sets + %s extra)\n", contador_paleta, i, bonus))
          contador_paleta <- contador_paleta + 1
          
        } else if (sets == 1) {
          # Canje por 3 dulces (1 set) -> 1 paleta
          estudiantes[[i]]["P"] <- 1
          estudiantes[[i]][c("A","B","C")] <- estudiantes[[i]][c("A","B","C")] - 1
          cat(sprintf("  Paleta #%d -> Estudiante %d (1 set)\n", contador_paleta, i))
          contador_paleta <- contador_paleta + 1
        }
      }
    }
    
    # 3. Regla de devolución (solo si ya tiene paleta)
    for (i in 1:9) {
      if (estudiantes[[i]]["P"] == 1 && runif(1) < 0.15) {
        estudiantes[[i]]["P"] <- 0
        devolucion <- sample(c("A","B","C"), 3, replace = TRUE)
        for (candy in devolucion) estudiantes[[i]][candy] <- estudiantes[[i]][candy] + 1
        cat(sprintf("  Estudiante %d devolvio su paleta -> obtuvo dulces %s\n", 
                    i, paste(devolucion, collapse=" ")))
      }
    }
    
    # 4. Condición de parada: todos con exactamente 1 paleta
    paletas_por_est <- sapply(estudiantes, function(e) e["P"])
    if (all(paletas_por_est == 1)) break
  }
  
  # 5. Resultado final
  cat("\nIteraciones totales:", iteraciones, "\n")
  tabla <- t(sapply(estudiantes, function(e) e))
  colnames(tabla) <- c("A","B","C","Paletas")
  print(as.data.frame(tabla))
  cat("\nTodos los estudiantes tienen exactamente UNA paleta\n")
}

# Ejecutar simulación
simular_paletas_unicas()
