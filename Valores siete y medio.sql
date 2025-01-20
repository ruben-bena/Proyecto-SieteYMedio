SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE `siete_y_medio`.`rounds`;
TRUNCATE TABLE `siete_y_medio`.`game_players`;
TRUNCATE TABLE `siete_y_medio`.`games`;
TRUNCATE TABLE `siete_y_medio`.`players`;
TRUNCATE TABLE `siete_y_medio`.`cards`;
TRUNCATE TABLE `siete_y_medio`.`decks`;
TRUNCATE TABLE `siete_y_medio`.`rounds_players`;

-- Insertar datos en la tabla `decks`
INSERT INTO `siete_y_medio`.`decks` (`deck_id`, `deck_name`)
VALUES 
  ('ESP', 'Baraja Española'),
  ('POKER', 'Baraja de Póker');

-- Insertar datos en la tabla `cards` para la baraja española
INSERT INTO cards (card_id, name, game_value, priority, real_value,deck_id) VALUES
("O01", "As de Oros", 1, 4, 1, "ESP"),
("O02", "Dos de Oros", 2, 4, 2, "ESP"),
("O03", "Tres de Oros", 3, 4, 3, "ESP"),
("O04", "Cuatro de Oros", 4, 4, 4, "ESP"),
("O05", "Cinco de Oros", 5, 4, 5, "ESP"),
("O06", "Seis de Oros", 6, 4, 6, "ESP"),
("O07", "Siete de Oros", 7, 4, 7, "ESP"),
("O08", "Ocho de Oros", 0.5, 4, 8, "ESP"),
("O09", "Nueve de Oros", 0.5, 4, 9, "ESP"),
("O10", "Sota de Oros", 0.5, 4, 10, "ESP"),
("O11", "Caballo de Oros", 0.5, 4, 11, "ESP"),
("O12", "Rey de Oros", 0.5, 4, 12, "ESP"),
("C01", "As de Copas", 1, 3, 1, "ESP"),
("C02", "Dos de Copas", 2, 3, 2, "ESP"),
("C03", "Tres de Copas", 3, 3, 3, "ESP"),
("C04", "Cuatro de Copas", 4, 3, 4, "ESP"),
("C05", "Cinco de Copas", 5, 3, 5, "ESP"),
("C06", "Seis de Copas", 6, 3, 6, "ESP"),
("C07", "Siete de Copas", 7, 3, 7, "ESP"),
("C08", "Ocho de Copas", 0.5, 3, 8, "ESP"),
("C09", "Nueve de Copas", 0.5, 3, 9, "ESP"),
("C10", "Sota de Copas", 0.5, 3, 10, "ESP"),
("C11", "Caballo de Copas", 0.5, 3, 11, "ESP"),
("C12", "Rey de Copas", 0.5, 3, 12, "ESP"),
("E01", "As de Espadas", 1, 2, 1, "ESP"),
("E02", "Dos de Espadas", 2, 2, 2, "ESP"),
("E03", "Tres de Espadas", 3, 2, 3, "ESP"),
("E04", "Cuatro de Espadas", 4, 2, 4, "ESP"),
("E05", "Cinco de Espadas", 5, 2, 5, "ESP"),
("E06", "Seis de Espadas", 6, 2, 6, "ESP"),
("E07", "Siete de Espadas", 7, 2, 7, "ESP"),
("E08", "Ocho de Espadas", 0.5, 2, 8, "ESP"),
("E09", "Nueve de Espadas", 0.5, 2, 9, "ESP"),
("E10", "Sota de Espadas", 0.5, 2, 10, "ESP"),
("E11", "Caballo de Espadas", 0.5, 2, 11, "ESP"),
("E12", "Rey de Espadas", 0.5, 2, 12, "ESP"),
("B01", "As de Bastos", 1, 1, 1, "ESP"),
("B02", "Dos de Bastos", 2, 1, 2, "ESP"),
("B03", "Tres de Bastos", 3, 1, 3, "ESP"),
("B04", "Cuatro de Bastos", 4, 1, 4, "ESP"),
("B05", "Cinco de Bastos", 5, 1, 5, "ESP"),
("B06", "Seis de Bastos", 6, 1, 6, "ESP"),
("B07", "Siete de Bastos", 7, 1, 7, "ESP"),
("B08", "Ocho de Bastos", 0.5, 1, 8, "ESP"),
("B09", "Nueve de Bastos", 0.5, 1, 9, "ESP"),
("B10", "Sota de Bastos", 0.5, 1, 10, "ESP"),
("B11", "Caballo de Bastos", 0.5, 1, 11, "ESP"),
("B12", "Rey de Bastos", 0.5, 1, 12, "ESP");
-- Insertar datos en la tabla `players`
INSERT INTO `siete_y_medio`.`players` (`player_id`, `name`, `is_ai`, `risk_level`)
VALUES
  (1, 'Jugador1', 0, 3),
  (2, 'Jugador2', 1, 5),
  (3, 'Jugador3', 0, 2),
  (4, 'Jugador4', 1, 4);

-- Insertar datos en la tabla `games`
INSERT INTO `siete_y_medio`.`games` (`game_id`, `start_time`, `end_time`, `deck_id`, `number_players`, `number_rounds`)
VALUES
  (1, '2025-01-13 10:00:00', '2025-01-13 11:00:00', 'ESP', 4, 5),
  (2, '2025-01-14 10:00:00', '2025-01-14 11:30:00', 'POKER', 3, 4);

-- Insertar datos en la tabla `game_players`
INSERT INTO `siete_y_medio`.`game_players` (`game_players_id`, `game_id`, `player_id`)
VALUES
  ('GP1', 1, 1),
  ('GP2', 1, 2),
  ('GP3', 1, 3),
  ('GP4', 1, 4),
  ('GP5', 2, 1),
  ('GP6', 2, 3),
  ('GP7', 2, 4);


INSERT INTO `siete_y_medio`.`rounds_players` 
(`round_id`, `game_id`, `round_number`, `player_id`, `first_cart_in_hand`, `player_start_points`, `player_end_points`, `player_bet`, `player_bank`) 
VALUES
-- Ronda 1
('1', 1, 1, 101, 'O01', 37, 68, 10, b'0'),
('2', 1, 1, 102, 'C02', 88, 44, 17, b'0'),
('3', 1, 1, 103, 'E03', 65, 90, 23, b'1'),
-- Ronda 2
('4', 1, 2, 101, 'B04', 54, 72, 14, b'0'),
('5', 1, 2, 102, 'O05', 83, 91, 25, b'0'),
('6', 1, 2, 103, 'C06', 62, 57, 8, b'1'),
-- Ronda 3
('7', 1, 3, 101, 'E07', 45, 98, 20, b'0'),
('8', 1, 3, 102, 'B08', 56, 75, 15, b'1'),
('9', 1, 3, 103, 'O09', 70, 65, 19, b'0'),
-- Ronda 4
('10', 1, 4, 101, 'C10', 87, 43, 12, b'1'),
('11', 1, 4, 102, 'E11', 69, 89, 9, b'0'),
('12', 1, 4, 103, 'B12', 92, 74, 16, b'0'),
-- Ronda 5
('13', 1, 5, 101, 'O01', 39, 76, 11, b'0'),
('14', 1, 5, 102, 'C02', 64, 92, 18, b'1'),
('15', 1, 5, 103, 'E03', 58, 53, 21, b'0'),
-- Ronda 1 - Partida 2
('16', 2, 1, 201, 'B04', 74, 89, 13, b'0'),
('17', 2, 1, 202, 'O05', 48, 64, 22, b'0'),
('18', 2, 1, 203, 'C06', 99, 78, 7, b'1'),
-- Ronda 2 - Partida 2
('19', 2, 2, 201, 'E07', 52, 83, 15, b'0'),
('20', 2, 2, 202, 'B08', 61, 94, 12, b'0'),
('21', 2, 2, 203, 'O09', 86, 49, 24, b'1'),
-- Ronda 3 - Partida 2
('22', 2, 3, 201, 'C10', 77, 72, 6, b'0'),
('23', 2, 3, 202, 'E11', 43, 65, 14, b'1'),
('24', 2, 3, 203, 'B12', 95, 81, 19, b'0'),
-- Ronda 4 - Partida 2
('25', 2, 4, 201, 'O01', 80, 60, 8, b'1'),
('26', 2, 4, 202, 'C02', 55, 97, 13, b'0'),
('27', 2, 4, 203, 'E03', 68, 79, 22, b'0'),
-- Ronda 5 - Partida 2
('28', 2, 5, 201, 'B04', 42, 50, 17, b'0'),
('29', 2, 5, 202, 'O05', 94, 88, 9, b'1'),
('30', 2, 5, 203, 'C06', 73, 63, 20, b'0'),
-- Ronda 1 - Partida 3
('31', 3, 1, 301, 'E07', 79, 70, 11, b'0'),
('32', 3, 1, 302, 'B08', 67, 85, 25, b'0'),
('33', 3, 1, 303, 'O09', 59, 41, 16, b'1'),
-- Ronda 2 - Partida 3
('34', 3, 2, 301, 'C10', 96, 87, 14, b'0'),
('35', 3, 2, 302, 'E11', 53, 98, 10, b'0'),
('36', 3, 2, 303, 'B12', 76, 66, 21, b'1'),
-- Ronda 3 - Partida 3
('37', 3, 3, 301, 'O01', 84, 73, 18, b'0'),
('38', 3, 3, 302, 'C02', 91, 93, 7, b'1'),
('39', 3, 3, 303, 'E03', 75, 62, 23, b'0'),
-- Ronda 4 - Partida 3
('40', 3, 4, 301, 'B04', 46, 71, 15, b'1'),
('41', 3, 4, 302, 'O05', 81, 90, 9, b'0'),
('42', 3, 4, 303, 'C06', 63, 54, 12, b'0'),
-- Ronda 5 - Partida 3
('43', 3, 5, 301, 'E07', 78, 82, 19, b'0'),
('44', 3, 5, 302, 'B08', 49, 95, 8, b'1'),
('45', 3, 5, 303, 'O09', 87, 45, 24, b'0');


  select * from rounds_players


