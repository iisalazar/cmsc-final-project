-- Creating database and tables
CREATE DATABASE IF NOT EXISTS splitwise_clone;
USE splitwise_clone;

CREATE TABLE IF NOT EXISTS person (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  isUser BOOLEAN NOT NULL DEFAULT FALSE,
  CONSTRAINT person_id_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS grp (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  dateCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT grp_id_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS person_grp (
  personId INT NOT NULL,
  grpId INT NOT NULL,
  CONSTRAINT person_grp_id_pk PRIMARY KEY (personId, grpId),
  CONSTRAINT person_grp_person_id_fk FOREIGN KEY (personId) REFERENCES person (id),
  CONSTRAINT person_grp_grp_id_fk FOREIGN KEY (grpId) REFERENCES grp (id)
);

CREATE TABLE IF NOT EXISTS transaction (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  amount INT NOT NULL,
  dateCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  personId INT,
  grpId INT,
  lenderId INT NOT NULL,
  lendeeId INT NOT NULL,
  type VARCHAR(255) NOT NULL,
  CONSTRAINT transaction_id_pk PRIMARY KEY (id),
  CONSTRAINT transaction_person_id_fk FOREIGN KEY (personId) REFERENCES person (id),
  CONSTRAINT transaction_grp_id_fk FOREIGN KEY (grpId) REFERENCES grp (id),
  CONSTRAINT transaction_lender_id_fk FOREIGN KEY (lenderId) REFERENCES person (id),
  CONSTRAINT transaction_lendee_id_fk FOREIGN KEY (lendeeId) REFERENCES person (id)
);


INSERT INTO person (name, isUser) 
VALUES 
  ('Ian', TRUE);
INSERT INTO person (name, isUser) 
VALUES 
  ('Kenneth', FALSE);
INSERT INTO person (name, isUser) 
VALUES 
  ('Jimwell', FALSE);
INSERT INTO person (name, isUser) 
VALUES 
  ('Quim', FALSE);
INSERT INTO person (name, isUser) 
VALUES 
  ('Hannah', FALSE);
INSERT INTO person (name, isUser) 
VALUES 
  ('Annie', FALSE);
INSERT INTO person (name, isUser) 
VALUES 
  ('Mark', FALSE);
INSERT INTO grp (name, dateCreated) 
VALUES 
  (
    'abc group', 
    CURDATE()
  ), 
  (
    'B Co.', 
    STR_TO_DATE(
      '2022-04-22T16:18:46.571Z', '%Y-%m-%dT%H:%i:%s.%fZ'
    )
  ), 
  (
    'Ken and Company', 
    STR_TO_DATE(
      '2021-02-14T10:43:31.121Z', '%Y-%m-%dT%H:%i:%s.%fZ'
    )
  ), 
  (
    'X Inc. colleagues', 
    STR_TO_DATE(
      '2023-01-11T17:21:11.987Z', '%Y-%m-%dT%H:%i:%s.%fZ'
    )
  ), 
  (
    'School Friends', 
    STR_TO_DATE(
      '2016-11-10T12:30:11.123Z', '%Y-%m-%dT%H:%i:%s.%fZ'
    )
  );
INSERT INTO person_grp 
VALUES 
  (1, 1), 
  (1, 2), 
  (1, 3), 
  (1, 4), 
  (1, 5), 
  (6, 1), 
  (6, 3), 
  (6, 4), 
  (3, 2), 
  (3, 1), 
  (4, 5), 
  (4, 3), 
  (5, 4), 
  (5, 5), 
  (5, 2);
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    '1-to-1 Expense 1', 200, NOW(), 1, 
    NULL, 1, 3, "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    '1-to-1 Expense 2', 150, NOW(), 1, 
    NULL, 1, 3, "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    '1-to-1 Expense 3', 250, NOW(), 3, 
    NULL, 3, 1, "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    '1-to-1 Expense 1 payment', 100, 
    NOW(), 1, NULL, 1, 3, "payment"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    '1-to-1 Expense 4', 250, NOW(), 3, 
    NULL, 3, 1, "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    'Group Expense 1', 
    600 /(
      select 
        count(grpId) 
      from 
        person_grp 
      where 
        grpId = 3
    ), 
    CURDATE(), 
    NULL, 
    3, 
    1, 
    4, 
    "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    'Group Expense 1', 
    600 /(
      select 
        count(grpId) 
      from 
        person_grp 
      where 
        grpId = 3
    ), 
    CURDATE(), 
    NULL, 
    3, 
    1, 
    6, 
    "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    'Group Expense 1', 
    200, 
    CURDATE(), 
    NULL, 
    3, 
    1, 
    6, 
    "payment"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    'Group Expense 2', 
    600 /(
      select 
        count(grpId) 
      from 
        person_grp 
      where 
        grpId = 3
    ), 
    CURDATE(), 
    NULL, 
    3, 
    1, 
    4, 
    "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    'Group Expense 2', 
    600 /(
      select 
        count(grpId) 
      from 
        person_grp 
      where 
        grpId = 3
    ), 
    CURDATE(), 
    NULL, 
    3, 
    1, 
    6, 
    "expense"
  );
INSERT INTO transaction (
  name, amount, dateCreated, personId, 
  grpId, lenderId, lendeeId, type
) 
VALUES 
  (
    'Group Expense 2', 
    200, 
    CURDATE(), 
    NULL, 
    3, 
    1, 
    6, 
    "payment"
  );

