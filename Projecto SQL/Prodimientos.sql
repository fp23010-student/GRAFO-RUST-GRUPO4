-- =============================================
-- 03_PROCEDIMIENTOS.SQL
-- =============================================

-- Procedimiento 1: Inscribir Materia
CREATE OR REPLACE PROCEDURE pr_inscribir_materia(
    p_carnet   IN VARCHAR2,
    p_carrera  IN VARCHAR2,
    p_plan     IN VARCHAR2,
    p_materia  IN VARCHAR2,
    p_grupo    IN VARCHAR2,
    p_ciclo    IN VARCHAR2
) IS
    v_existe NUMBER;
    v_pertenece NUMBER;
    v_matricula NUMBER;
BEGIN
    -- Validar alumno
    SELECT COUNT(*) INTO v_existe FROM ALUMNO WHERE CARNET = p_carnet;
    IF v_existe = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El alumno no existe.');
    END IF;

    -- Validar pertenece al plan
    SELECT COUNT(*) INTO v_pertenece 
      FROM PERTENECE 
     WHERE CARNET = p_carnet AND COD_CARRERA = p_carrera AND PLAN = p_plan;
     
    IF v_pertenece = 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'El alumno no pertenece al plan indicado.');
    END IF;

    v_matricula := fn_calcularMatricula(p_carnet, p_materia, p_carrera, p_plan);

    INSERT INTO INSCRIPCION (CARNET, COD_CARRERA, PLAN, COD_MATERIA, GRUPO, CICLO, MATRICULA)
    VALUES (p_carnet, p_carrera, p_plan, p_materia, p_grupo, p_ciclo, v_matricula);

    DBMS_OUTPUT.PUT_LINE('Inscripción exitosa. Matrícula: ' || v_matricula);
END pr_inscribir_materia;
/

-- Procedimiento 2: Cierre de Ciclo
CREATE OR REPLACE PROCEDURE pr_cierre_ciclo(p_anhociclo IN VARCHAR2) IS
    CURSOR c_insc IS
        SELECT * FROM INSCRIPCION WHERE CICLO = p_anhociclo;

    v_estado VARCHAR2(20);
BEGIN
    FOR reg IN c_insc LOOP
        IF reg.NOTA_FINAL >= 6.0 THEN
            v_estado := 'APROBADA';
        ELSE
            v_estado := 'REPROBADA';
        END IF;

        INSERT INTO EXPEDIENTE (CARNET, COD_MATERIA, COD_CARRERA, PLAN, NOTA, ESTADO, CICLO)
        VALUES (reg.CARNET, reg.COD_MATERIA, reg.COD_CARRERA, reg.PLAN, 
                reg.NOTA_FINAL, v_estado, reg.CICLO);
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('Cierre de ciclo ' || p_anhociclo || ' completado.');
END pr_cierre_ciclo;
/

-- Procedimiento 3: Reporte Docente
CREATE OR REPLACE PROCEDURE pr_reporte_docente(p_ciclo_anho IN VARCHAR2) IS
    CURSOR c_doc IS
        SELECT d.NOMBRE, COUNT(i.CARNET) AS total
          FROM DOCENTE d
          JOIN GRUPO g ON d.COD_DOCENTE = g.COD_DOCENTE
          JOIN INSCRIPCION i ON g.COD_GRUPO = i.GRUPO 
                            AND g.COD_MATERIA = i.COD_MATERIA
         WHERE i.CICLO = p_ciclo_anho
         GROUP BY d.NOMBRE;
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== REPORTE DOCENTES - Ciclo: ' || p_ciclo_anho || ' ===');
    FOR reg IN c_doc LOOP
        DBMS_OUTPUT.PUT_LINE('Docente: ' || RPAD(reg.NOMBRE, 35) || ' | Alumnos: ' || reg.total);
    END LOOP;
END pr_reporte_docente;
/

SHOW ERRORS;
PROMPT 'Procedimientos creados correctamente.';