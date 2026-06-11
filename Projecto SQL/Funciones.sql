-- =============================================
-- 02_FUNCIONES.SQL
-- =============================================

-- Función 1: Calcular CUM
CREATE OR REPLACE FUNCTION calcularCUM(
    p_carnet      IN VARCHAR2,
    p_codCarrera  IN VARCHAR2,
    p_plan        IN VARCHAR2
) RETURN NUMBER IS
    v_cum NUMBER;
BEGIN
    SELECT ROUND(SUM(e.NOTA * m.UV) / NULLIF(SUM(m.UV), 0), 2)
      INTO v_cum
      FROM EXPEDIENTE e
      JOIN MATERIA m ON e.COD_MATERIA = m.COD_MATERIA
     WHERE e.CARNET = p_carnet
       AND e.COD_CARRERA = p_codCarrera
       AND e.PLAN = p_plan
       AND e.ESTADO = 'APROBADA';

    RETURN NVL(v_cum, 0);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 0;
    WHEN OTHERS THEN
        RETURN 0;
END calcularCUM;
/

-- Función 2: Validar Prerrequisito
CREATE OR REPLACE FUNCTION fn_valida_prerrequisito(
    p_carnet    IN VARCHAR2,
    p_materia   IN VARCHAR2,
    p_carrera   IN VARCHAR2,
    p_plan      IN VARCHAR2
) RETURN NUMBER IS
    v_cumple NUMBER := 1;
BEGIN
    FOR r IN (
        SELECT COD_PRERREQ 
          FROM PRERREQUISITO 
         WHERE COD_MATERIA = p_materia 
           AND COD_CARRERA = p_carrera 
           AND PLAN = p_plan
    ) LOOP
        SELECT COUNT(*) INTO v_cumple
          FROM EXPEDIENTE
         WHERE CARNET = p_carnet
           AND COD_MATERIA = r.COD_PRERREQ
           AND COD_CARRERA = p_carrera
           AND PLAN = p_plan
           AND ESTADO = 'APROBADA';

        IF v_cumple = 0 THEN
            RETURN 0;
        END IF;
    END LOOP;
    RETURN 1;
END fn_valida_prerrequisito;
/

-- Función 3: Calcular Matrícula
CREATE OR REPLACE FUNCTION fn_calcularMatricula(
    p_carnet    IN VARCHAR2,
    p_materia   IN VARCHAR2,
    p_carrera   IN VARCHAR2,
    p_plan      IN VARCHAR2
) RETURN NUMBER IS
    v_max NUMBER;
BEGIN
    SELECT NVL(MAX(MATRICULA), 0) + 1
      INTO v_max
      FROM EXPEDIENTE
     WHERE CARNET = p_carnet
       AND COD_MATERIA = p_materia
       AND COD_CARRERA = p_carrera
       AND PLAN = p_plan;

    RETURN v_max;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 1;
END fn_calcularMatricula;
/

SHOW ERRORS;
PROMPT 'Funciones creadas correctamente.';