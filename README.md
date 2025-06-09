Tabelul Clienti
CREATE TABLE Clienti (
  IdClient INT PRIMARY KEY,
  Nume VARCHAR(50) NOT NULL,
  Prenume VARCHAR(50) NOT NULL,
  Adresa VARCHAR(100) NOT NULL,
  CNP VARCHAR(14) NOT NULL,
  Email VARCHAR(100) UNIQUE,
  Telefon VARCHAR(10) NOT NULL,
  StareFinanciara VARCHAR(15) CHECK (StareFinanciara IN ('la zi', 'restanțier'))
);


INSERT INTO Clienti (IdClient, Nume, Prenume, Adresa, CNP, Email, Telefon, StareFinanciara) VALUES (1, 'Belu', 'Florentina-Alexanda', 'Camin Leu A Bucuresti', '1981230123456', 'f.belu@email.com', '0712345678', 'la zi'), (2, 'Ion', 'Ion', 'Str. Lalelelor nr. 8, Timișoara', '2345678901234', 'ion.ion@email.com', '0722001100', 'la zi'),
(3, 'Daniel', 'Mihai', 'Bd. Revoluției nr. 5, Arad', '1870523123456', 'daniel.mihai@email.com', '0744111222', 'restanțier'), (4, 'Elena', 'Pop', 'Str. Zorilor 21, Brașov', '2981112223344', 'elena.pop@email.com',     '0755222333', 'la zi');
Tabelul Abonamente
CREATE TABLE Abonamente (
  IdAbonament INT PRIMARY KEY,
  TipAbonament VARCHAR(50) NOT NULL,
  Cost DECIMAL(6,2) CHECK (Cost >= 0),
  StarePlata VARCHAR(15) CHECK (StarePlata IN ('la zi', 'restanțier')),
  VechimeLuni INT CHECK (VechimeLuni >= 0),
  IdClient INT NOT NULL,
  IdServiciu INT NOT NULL,
  IdTarif INT NOT NULL,
  CONSTRAINT fk_client_abonament FOREIGN KEY (IdClient) REFERENCES Clienti(IdClient),
  CONSTRAINT fk_serviciu_abonament FOREIGN KEY (IdServiciu) REFERENCES Servicii(IdServiciu),
  CONSTRAINT fk_tarif_abonament FOREIGN KEY (IdTarif) REFERENCES Tarife(IdTarif)
);

INSERT INTO Abonamente VALUES (1, 'StudentPlus', 30.00, 'la zi', 4, 1, 1, 1), (2, 'SmarrtNet', 40.00, 'la zi', 6, 2, 2, 2), (3, 'BusinessX', 70.00, 'restanțier', 18, 3, 3, 3), (4, 'MiniStart', 25.00, 'la zi', 2, 4, 1, 1);


Tabelul CartelePreplatite
CREATE TABLE CartelePreplatite (
  IdPrepay INT PRIMARY KEY,
  SumaDisponibila DECIMAL(6,2) CHECK (SumaDisponibila >= 0),
  VechimeLuni INT CHECK (VechimeLuni >= 0),
  IdClient INT NOT NULL,
  IdServiciu INT NOT NULL,
  CONSTRAINT fk_client_prepay FOREIGN KEY (IdClient) REFERENCES Clienti(IdClient),
  CONSTRAINT fk_serviciu_prepay FOREIGN KEY (IdServiciu) REFERENCES Servicii(IdServiciu)
);
INSERT INTO CartelePreplatite VALUES (1, 20.00, 6, 1, 1), (2, 15.00, 3, 2, 2), (3, 30.00, 12, 3, 1), (4, 5.00, 1, 4, 3);
Tabelul Servicii
CREATE TABLE Servicii (
  IdServiciu INT PRIMARY KEY,
  Voce BOOLEAN NOT NULL,
  SMS BOOLEAN NOT NULL,
  MMS BOOLEAN NOT NULL,
  VideoCall BOOLEAN NOT NULL,
  Internet BOOLEAN NOT NULL,
  Roaming BOOLEAN NOT NULL
);
INSERT INTO Servicii VALUES (1, 1, 1, 1, 1, 1, 1), (2, 1, 1, 1, 0, 0, 0), (3, 0, 0, 1, 1, 1, 1),  (4, 0, 0, 0, 0, 0, 0);

Tabelul Tarife
CREATE TABLE Tarife (
  IdTarif INT PRIMARY KEY,
  ApelRetea DECIMAL(5,2) CHECK (ApelRetea >= 0),
  ApelExtraRetea DECIMAL(5,2) CHECK (ApelExtraRetea >= 0),
  SMSRetea DECIMAL(5,2) CHECK (SMSRetea >= 0),
  SMSExtraRetea DECIMAL(5,2) CHECK (SMSExtraRetea >= 0),
  MMS DECIMAL(5,2) CHECK (MMS >= 0),
  TraficInternet DECIMAL(6,4) CHECK (TraficInternet >= 0)
);
INSERT INTO Tarife VALUES
(1, 0.05, 0.10, 0.02, 0.05, 0.10, 0.0015),  -- Tarif standard
(2, 0.03, 0.08, 0.01, 0.04, 0.08, 0.0010),  -- Tarif student
(3, 0.06, 0.12, 0.03, 0.06, 0.12, 0.0020);  -- Tarif business

INSERT INTO Tarife VALUES (1, 0.05, 0.10, 0.02, 0.05, 0.10, 0.0015), (2, 0.03, 0.08, 0.01, 0.04, 0.08, 0.0010), (3, 0.06, 0.12, 0.03, 0.06, 0.12, 0.0020);  
Tabelul Contracte
CREATE TABLE Contracte (
  IdContract INT PRIMARY KEY,
  DataInceput DATE NOT NULL,
  DataSfarsit DATE NOT NULL,
  IdClient INT NOT NULL,
  IdAbonament INT UNIQUE NOT NULL,
  CONSTRAINT fk_client_contract FOREIGN KEY (IdClient) REFERENCES Clienti(IdClient),
  CONSTRAINT fk_abonament_contract FOREIGN KEY (IdAbonament) REFERENCES Abonamente(IdAbonament)
);

INSERT INTO Contracte VALUES (1, '2024-01-01', '2025-01-01', 1, 1), (2, '2024-02-01', '2025-02-01', 2, 2), (3, '2023-08-15', '2025-08-15', 3, 3), (4, '2024-05-10', '2025-05-10', 4, 4);
Tabelul Facturi
CREATE TABLE Facturi (
  IdFactura INT PRIMARY KEY,
  DataEmitere DATE NOT NULL,
  DataScadenta DATE NOT NULL,
  TotalPlata DECIMAL(6,2) CHECK (TotalPlata >= 0),
  IdClient INT NOT NULL,
  IdAbonament INT NOT NULL,
  CONSTRAINT fk_client_factura FOREIGN KEY (IdClient) REFERENCES Clienti(IdClient),
  CONSTRAINT fk_abonament_factura FOREIGN KEY (IdAbonament) REFERENCES Abonamente(IdAbonament)
);

INSERT INTO Facturi VALUES (1, '2024-02-01', '2024-02-10', 50.00, 1, 1), (2, '2024-03-01', '2024-03-10', 35.00, 2, 2), (3, '2024-04-01', '2024-04-10', 70.00, 3, 3), (4, '2024-05-01', '2024-05-10', 25.00, 4, 4);
Tabelul NumereTelefon
CREATE TABLE NumereTelefon (
  NumarTelefon VARCHAR(10) PRIMARY KEY,
  IdClient INT NOT NULL,
  IdAbonament INT UNIQUE,
  IdPrepay INT UNIQUE,
  CONSTRAINT fk_client_numar FOREIGN KEY (IdClient) REFERENCES Clienti(IdClient),
  CONSTRAINT fk_abonament_numar FOREIGN KEY (IdAbonament) REFERENCES Abonamente(IdAbonament),
  CONSTRAINT fk_prepay_numar FOREIGN KEY (IdPrepay) REFERENCES CartelePreplatite(IdPrepay),
  CONSTRAINT ck_tip_serviciu_exclusiv CHECK (
    (IdAbonament IS NULL AND IdPrepay IS NOT NULL) OR
    (IdAbonament IS NOT NULL AND IdPrepay IS NULL)
  )
);
INSERT INTO NumereTelefon VALUES ('0722123456', 1, 1, NULL), ('0744111222', 2, 2, NULL), ('0766333444', 3, 3, NULL),  ('0777222333', 2, NULL, 2);


Vederi
1.
CREATE VIEW V_ClientiRoaming AS
SELECT C.IdClient, C.Nume, C.Prenume, 'Abonament' AS Tip,
       N.NumarTelefon, S.Roaming
FROM Clienti C
JOIN Abonamente A ON C.IdClient = A.IdClient
JOIN Servicii S ON A.IdServiciu = S.IdServiciu
JOIN NumereTelefon N ON A.IdAbonament = N.IdAbonament
WHERE S.Roaming = 1

UNION

SELECT C.IdClient, C.Nume, C.Prenume, 'Prepay' AS Tip,
       N.NumarTelefon, S.Roaming
FROM Clienti C
JOIN CartelePreplatite P ON C.IdClient = P.IdClient
JOIN Servicii S ON P.IdServiciu = S.IdServiciu
JOIN NumereTelefon N ON P.IdPrepay = N.IdPrepay
WHERE S.Roaming = 1;

2.
CREATE VIEW V_ClientiRestantieri AS
SELECT DISTINCT C.IdClient, C.Nume, C.Prenume, C.StareFinanciara
FROM Clienti C
JOIN Abonamente A ON C.IdClient = A.IdClient
WHERE A.StarePlata = 'restanțier' OR C.StareFinanciara = 'restanțier';

3.
CREATE VIEW V_ClientiVechi AS
SELECT C.IdClient, C.Nume, C.Prenume, A.VechimeLuni AS Vechime, 'Abonament' AS Tip
FROM Clienti C
JOIN Abonamente A ON C.IdClient = A.IdClient
WHERE A.VechimeLuni > 3

UNION

SELECT C.IdClient, C.Nume, C.Prenume, P.VechimeLuni, 'Prepay' AS Tip
FROM Clienti C
JOIN CartelePreplatite P ON C.IdClient = P.IdClient
WHERE P.VechimeLuni > 3;

# soa
