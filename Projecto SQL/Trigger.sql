-- =============================================
-- 04_TRIGGERS.SQL
-- =============================================

-- Trigger 1: Verificar Cupo
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

-- Trigger 2: Auditar Expediente
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

-- Trigger 3: Verificar Tupla Expediente
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

SHOW ERRORS;
PROMPT 'Triggers creados correctamente.';