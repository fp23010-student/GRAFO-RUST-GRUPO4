-- =============================================
-- IMPLEMENTACIÓN PROMETEO
-- Nombre: [Tu Nombre Completo]
-- Carnet: [Tu Carnet]
-- Fecha: [Fecha Actual]
-- =============================================

SET SERVEROUTPUT ON;
PROMPT '=== INICIANDO CREACIÓN DE OBJETOS PROMETEO ===';

-- =============================================
-- 1. TABLAS AUXILIARES
-- =============================================
PROMPT 'Creando tablas auxiliares...';

CREATE TABLE PRERREQUISITO (
    COD_MATERIA     VARCHAR2(10),
    COD_PRERREQ     VARCHAR2(10),
    COD_CARRERA     VARCHAR2(10),
    PLAN            VARCHAR2(10),
    CONSTRAINT PK_PRERREQUISITO 
        PRIMARY KEY (COD_MATERIA, COD_PRERREQ, COD_CARRERA, PLAN)
);

CREATE TABLE AUDITORIA_NOTAS_EXPEDIENTE (
    ID_AUDITORIA    NUMBER GENERATED ALWAYS AS IDENTITY,
    CARNET          VARCHAR2(10),
    COD_MATERIA     VARCHAR2(10),
    COD_CARRERA     VARCHAR2(10),
    PLAN            VARCHAR2(10),
    NOTA_ANTERIOR   NUMBER(4,2),
    NOTA_NUEVA      NUMBER(4,2),
    USUARIO         VARCHAR2(30) DEFAULT USER,
    FECHA           DATE         DEFAULT SYSDATE,
    CONSTRAINT PK_AUDITORIA_EXPEDIENTE 
        PRIMARY KEY (ID_AUDITORIA)
);

-- =============================================
-- 2. FUNCIONES
-- =============================================
PROMPT 'Creando funciones...';

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
    WHEN NO_DATA_FOUND THEN RETURN 0;
    WHEN OTHERS THEN RETURN 0;
END calcularCUM;
/

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
    WHEN NO_DATA_FOUND THEN RETURN 1;
END fn_calcularMatricula;
/

-- =============================================
-- 3. PROCEDIMIENTOS
-- =============================================
PROMPT 'Creando procedimientos...';

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
    SELECT COUNT(*) INTO v_existe FROM ALUMNO WHERE CARNET = p_carnet;
    IF v_existe = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El alumno no existe.');
    END IF;

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
    DBMS_OUTPUT.PUT_LINE('=== REPORTE DOCENTES - Ciclo: ' || p_ciclo_anño || ' ===');
    FOR reg IN c_doc LOOP
        DBMS_OUTPUT.PUT_LINE('Docente: ' || RPAD(reg.NOMBRE, 35) || ' | Alumnos: ' || reg.total);
    END LOOP;
END pr_reporte_docente;
/

-- =============================================
-- 4. TRIGGERS
-- =============================================
PROMPT 'Creando triggers...';

CREATE OR REPLACE TRIGGER tr_verificar_cupo
BEFORE INSERT ON INSCRIPCION
FOR EACH ROW
DECLARE
    v_inscritos NUMBER;
    v_cupo      NUMBER;
BEGIN
    SELECT COUNT(*), CUPO 
      INTO v_inscritos, v_cupo
      FROM GRUPO 
     WHERE COD_GRUPO = :NEW.GRUPO 
       AND COD_MATERIA = :NEW.COD_MATERIA;

    IF v_inscritos >= v_cupo THEN
        RAISE_APPLICATION_ERROR(-20003, 'El grupo ya alcanzó su cupo máximo.');
    END IF;
END tr_verificar_cupo;
/

CREATE OR REPLACE TRIGGER tr_audita_expediente
AFTER UPDATE OF NOTA ON EXPEDIENTE
FOR EACH ROW
BEGIN
    IF :OLD.ESTADO IN ('APROBADA', 'REPROBADA') THEN
        INSERT INTO AUDITORIA_NOTAS_EXPEDIENTE 
        (CARNET, COD_MATERIA, COD_CARRERA, PLAN, NOTA_ANTERIOR, NOTA_NUEVA)
        VALUES (:OLD.CARNET, :OLD.COD_MATERIA, :OLD.COD_CARRERA, :OLD.PLAN, 
                :OLD.NOTA, :NEW.NOTA);
    END IF;
END tr_audita_expediente;
/

CREATE OR REPLACE TRIGGER tr_verificar_tupla_expediente
BEFORE INSERT ON EXPEDIENTE
FOR EACH ROW
DECLARE
    v_existe NUMBER;
BEGIN
    IF :NEW.ESTADO != 'EQUIVALENCIA' THEN
        SELECT COUNT(*) INTO v_existe
          FROM INSCRIPCION
         WHERE CARNET = :NEW.CARNET
           AND COD_MATERIA = :NEW.COD_MATERIA
           AND COD_CARRERA = :NEW.COD_CARRERA
           AND PLAN = :NEW.PLAN;

        IF v_existe = 0 THEN
            RAISE_APPLICATION_ERROR(-20004, 'Debe existir una inscripción previa para esta materia (no equivalencia).');
        END IF;
    END IF;
END tr_verificar_tupla_expediente;
/

-- =============================================
-- FINALIZACIÓN
-- =============================================
PROMPT '=== VERIFICANDO ERRORES ===';
SHOW ERRORS;

SELECT OBJECT_NAME, OBJECT_TYPE, STATUS 
  FROM USER_OBJECTS 
 WHERE OBJECT_TYPE IN ('FUNCTION','PROCEDURE','TRIGGER','TABLE')
   AND STATUS = 'INVALID';

PROMPT '=== IMPLEMENTACIÓN PROMETEO FINALIZADA ===';
COMMIT;