-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema siete_y_medio
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema siete_y_medio
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `siete_y_medio` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `siete_y_medio` ;

-- -----------------------------------------------------
-- Table `siete_y_medio`.`decks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`decks` (
  `deck_id` VARCHAR(45) NOT NULL,
  `deck_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`deck_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`cards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`cards` (
  `card_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `deck_id` VARCHAR(45) NOT NULL,
  `real_value` INT NOT NULL,
  `game_value` INT NOT NULL,
  `priority` INT NULL DEFAULT NULL,
  PRIMARY KEY (`card_id`),
  INDEX `fk_Cards_Decks1_idx` (`deck_id` ASC) VISIBLE,
  CONSTRAINT `fk_Cards_Decks1`
    FOREIGN KEY (`deck_id`)
    REFERENCES `siete_y_medio`.`decks` (`deck_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`players` (
  `player_id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `is_ai` BIT(1) NOT NULL,
  `risk_level` INT UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`player_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`games` (
  `game_id` INT UNSIGNED NOT NULL,
  `start_time` TIMESTAMP NOT NULL,
  `end_time` TIMESTAMP NOT NULL,
  `deck_id` VARCHAR(45) NOT NULL DEFAULT 'ESP',
  `number_players` INT NOT NULL,
  `number_rounds` INT NOT NULL,
  PRIMARY KEY (`game_id`),
  INDEX `fk_games_decks1_idx` (`deck_id` ASC) VISIBLE,
  CONSTRAINT `fk_games_decks1`
    FOREIGN KEY (`deck_id`)
    REFERENCES `siete_y_medio`.`decks` (`deck_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`game_players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`game_players` (
  `game_players_id` VARCHAR(45) NOT NULL,
  `game_id` INT UNSIGNED NOT NULL,
  `player_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`game_players_id`),
  INDEX `fk_game_players_game_idx` (`game_id` ASC) VISIBLE,
  INDEX `fk_game_players_player_idx` (`player_id` ASC) VISIBLE,
  INDEX `idx_game_id_player_id` (`game_id` ASC, `player_id` ASC) VISIBLE,
  CONSTRAINT `fk_Game_has_players_players1`
    FOREIGN KEY (`player_id`)
    REFERENCES `siete_y_medio`.`players` (`player_id`),
  CONSTRAINT `fk_Games_has_players_games1`
    FOREIGN KEY (`game_id`)
    REFERENCES `siete_y_medio`.`games` (`game_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`inventory` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL DEFAULT NULL,
  `quantity` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id` (`id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`rounds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`rounds` (
  `round_id` INT UNSIGNED NOT NULL,
  `game_id` INT UNSIGNED NOT NULL,
  `round_number` INT UNSIGNED NOT NULL,
  `player_id` INT UNSIGNED NOT NULL,
  `player_start_points` INT NOT NULL,
  `player_end_points` INT NOT NULL,
  `player_bet` INT NULL DEFAULT NULL,
  `player_bank` BIT(1) NOT NULL,
  PRIMARY KEY (`round_id`),
  INDEX `fk_Rounds_games_players_idx` (`player_id` ASC, `game_id` ASC) VISIBLE,
  CONSTRAINT `fk_Rounds_games_players1`
    FOREIGN KEY (`player_id` , `game_id`)
    REFERENCES `siete_y_medio`.`game_players` (`game_id` , `player_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`rounds_players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`rounds_players` (
  `round_id` VARCHAR(45) NOT NULL,
  `game_id` INT UNSIGNED NOT NULL,
  `round_number` INT UNSIGNED NOT NULL,
  `player_id` INT UNSIGNED NOT NULL,
  `first_cart_in_hand` VARCHAR(45) NOT NULL,
  `player_start_points` INT NOT NULL,
  `player_end_points` INT NOT NULL,
  `player_bet` INT NULL DEFAULT NULL,
  `player_bank` BIT(1) NOT NULL,
  PRIMARY KEY (`round_id`),
  INDEX `fk_game_players_game_idx` (`game_id` ASC) VISIBLE,
  INDEX `fk_game_players_player_idx` (`player_id` ASC) VISIBLE,
  INDEX `idx_game_id_player_id` (`game_id` ASC, `player_id` ASC) VISIBLE,
  INDEX `fk_rounds_players_first_cart_in_hand_idx` (`first_cart_in_hand` ASC) VISIBLE,
  CONSTRAINT `fk_rounds_players_first_cart_in_hand`
    FOREIGN KEY (`first_cart_in_hand`)
    REFERENCES `siete_y_medio`.`cards` (`card_id`),
  CONSTRAINT `fk_Rounds_players_games1`
    FOREIGN KEY (`game_id`)
    REFERENCES `siete_y_medio`.`games` (`game_id`),
  CONSTRAINT `fk_Rounds_players_players1`
    FOREIGN KEY (`player_id`)
    REFERENCES `siete_y_medio`.`players` (`player_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `siete_y_medio` ;

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`info_player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`info_player` (`player_id` INT, `name` INT, `Total Points` INT, `Total games` INT, `Total minutes` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe` (`identificador_jugador` INT, `palo_carta_inicial_mas_repetida` INT, `carta_inicial_mas_repetida` INT, `numero_veces_repetida` INT, `total_partidas_jugadas` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_1` (`identificador_jugador` INT, `palo_carta_inicial_mas_repetida` INT, `carta_inicial_mas_repetida` INT, `numero_veces_repetida` INT, `total_partidas_jugadas` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_10`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_10` (`game_id` INT, `avg(player_bet)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_2` (`game_id` INT, `player_id` INT, `max(player_bet)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_3`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_3` (`game_id` INT, `player_id` INT, `min(player_bet)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_5`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_5` (`game_id` INT, `puntos_ganados` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_6`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_6` (`game_id` INT, `bank_wins` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_7`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_7` (`game_id` INT, `count(player_bank)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_8`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_8` (`game_id` INT, `avg(player_bet)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`informe_9`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`informe_9` (`game_id` INT, `avg(player_bet)` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`player_game_minutes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`player_game_minutes` (`player_id` INT, `player_name` INT, `game_id` INT, `total_minutes` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`player_statistics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`player_statistics` (`player_id` INT, `player_name` INT, `earnings` INT, `games_played` INT, `minutes_played` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`players_ranking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`players_ranking` (`player_id` INT, `player_name` INT, `total_gains` INT, `games_played` INT, `total_minutes` INT);

-- -----------------------------------------------------
-- Placeholder table for view `siete_y_medio`.`total_player_minutes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`total_player_minutes` (`player_id` INT, `name` INT, `total_minutes_played` INT);

-- -----------------------------------------------------
-- View `siete_y_medio`.`info_player`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`info_player`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`info_player` AS select `rp`.`player_id` AS `player_id`,`p`.`name` AS `name`,(sum(`rp`.`player_end_points`) - sum(`rp`.`player_start_points`)) AS `Total Points`,count(distinct `rp`.`game_id`) AS `Total games`,sum(timestampdiff(MINUTE,`g`.`start_time`,`g`.`end_time`)) AS `Total minutes` from ((`siete_y_medio`.`rounds_players` `rp` join `siete_y_medio`.`players` `p` on((`rp`.`player_id` = `p`.`player_id`))) join `siete_y_medio`.`games` `g` on((`rp`.`game_id` = `g`.`game_id`))) group by `rp`.`player_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe` AS select `p`.`player_id` AS `identificador_jugador`,substring_index(`c`.`name`,' ',1) AS `palo_carta_inicial_mas_repetida`,substring_index(`c`.`name`,' ',-(1)) AS `carta_inicial_mas_repetida`,count(`rp`.`first_cart_in_hand`) AS `numero_veces_repetida`,count(distinct `rp`.`game_id`) AS `total_partidas_jugadas` from ((`siete_y_medio`.`players` `p` join `siete_y_medio`.`rounds_players` `rp` on((`p`.`player_id` = `rp`.`player_id`))) join `siete_y_medio`.`cards` `c` on((`rp`.`first_cart_in_hand` = `c`.`card_id`))) group by `p`.`player_id`,`rp`.`first_cart_in_hand` order by `p`.`player_id`,`numero_veces_repetida` desc;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_1`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_1` AS select `p`.`player_id` AS `identificador_jugador`,substring_index(`c`.`name`,' ',1) AS `palo_carta_inicial_mas_repetida`,substring_index(`c`.`name`,' ',-(1)) AS `carta_inicial_mas_repetida`,count(`rp`.`first_cart_in_hand`) AS `numero_veces_repetida`,count(distinct `rp`.`game_id`) AS `total_partidas_jugadas` from ((`siete_y_medio`.`players` `p` join `siete_y_medio`.`rounds_players` `rp` on((`p`.`player_id` = `rp`.`player_id`))) join `siete_y_medio`.`cards` `c` on((`rp`.`first_cart_in_hand` = `c`.`card_id`))) group by `p`.`player_id`,`rp`.`first_cart_in_hand` order by `p`.`player_id`,`numero_veces_repetida` desc;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_10`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_10`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_10` AS select `r`.`game_id` AS `game_id`,avg(`r`.`player_bet`) AS `avg(player_bet)` from `siete_y_medio`.`rounds_players` `r` where `r`.`round_number` in (select max(`r`.`round_number`) from `siete_y_medio`.`rounds_players` `r` group by `r`.`game_id`) group by `r`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_2`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_2`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_2` AS select `r`.`game_id` AS `game_id`,`r`.`player_id` AS `player_id`,max(`r`.`player_bet`) AS `max(player_bet)` from `siete_y_medio`.`rounds_players` `r` group by `r`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_3`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_3`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_3` AS select `r`.`game_id` AS `game_id`,`r`.`player_id` AS `player_id`,min(`r`.`player_bet`) AS `min(player_bet)` from `siete_y_medio`.`rounds_players` `r` group by `r`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_5`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_5`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_5` AS select `ganadores`.`game_id` AS `game_id`,`ganadores`.`puntos_ganados` AS `puntos_ganados` from ((select `rp`.`game_id` AS `game_id`,`rp`.`player_id` AS `player_id`,max((`rp`.`player_end_points` - `rp`.`player_start_points`)) AS `puntos_ganados` from (`siete_y_medio`.`rounds_players` `rp` join `siete_y_medio`.`players` `p` on((`rp`.`player_id` = `p`.`player_id`))) group by `rp`.`game_id`) `ganadores` join `siete_y_medio`.`players` `p` on((`ganadores`.`player_id` = `p`.`player_id`))) where (`p`.`is_ai` = 1);

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_6`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_6`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_6` AS select `rp`.`game_id` AS `game_id`,count((case when ((`rp`.`player_bank` = 1) and (`rp`.`player_end_points` > `rp`.`player_start_points`)) then 1 end)) AS `bank_wins` from `siete_y_medio`.`rounds_players` `rp` group by `rp`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_7`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_7`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_7` AS select `siete_y_medio`.`rounds_players`.`game_id` AS `game_id`,count(`siete_y_medio`.`rounds_players`.`player_bank`) AS `count(player_bank)` from `siete_y_medio`.`rounds_players` group by `siete_y_medio`.`rounds_players`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_8`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_8`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_8` AS select `r`.`game_id` AS `game_id`,avg(`r`.`player_bet`) AS `avg(player_bet)` from `siete_y_medio`.`rounds_players` `r` group by `r`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`informe_9`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`informe_9`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`informe_9` AS select `r`.`game_id` AS `game_id`,avg(`r`.`player_bet`) AS `avg(player_bet)` from `siete_y_medio`.`rounds_players` `r` where (`r`.`round_number` = 1) group by `r`.`game_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`player_game_minutes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`player_game_minutes`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`player_game_minutes` AS select `gp`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,`g`.`game_id` AS `game_id`,timestampdiff(MINUTE,`g`.`start_time`,`g`.`end_time`) AS `total_minutes` from ((`siete_y_medio`.`games` `g` join `siete_y_medio`.`game_players` `gp` on((`g`.`game_id` = `gp`.`game_id`))) join `siete_y_medio`.`players` `p` on((`gp`.`player_id` = `p`.`player_id`))) group by `gp`.`player_id`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`player_statistics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`player_statistics`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`player_statistics` AS select `p`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,sum((`rp`.`player_end_points` - `rp`.`player_start_points`)) AS `earnings`,count(distinct `rp`.`game_id`) AS `games_played`,sum(timestampdiff(MINUTE,`g`.`start_time`,`g`.`end_time`)) AS `minutes_played` from ((`siete_y_medio`.`players` `p` join `siete_y_medio`.`rounds_players` `rp` on((`p`.`player_id` = `rp`.`player_id`))) join `siete_y_medio`.`games` `g` on((`rp`.`game_id` = `g`.`game_id`))) group by `p`.`player_id`,`p`.`name`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`players_ranking`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`players_ranking`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`players_ranking` AS select `p`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,sum((`rp`.`player_end_points` - `rp`.`player_start_points`)) AS `total_gains`,count(distinct `g`.`game_id`) AS `games_played`,sum(timestampdiff(MINUTE,`g`.`start_time`,`g`.`end_time`)) AS `total_minutes` from ((`siete_y_medio`.`players` `p` join `siete_y_medio`.`rounds_players` `rp` on((`p`.`player_id` = `rp`.`player_id`))) join `siete_y_medio`.`games` `g` on((`rp`.`game_id` = `g`.`game_id`))) where ((`g`.`start_time` is not null) and (`g`.`end_time` is not null)) group by `p`.`player_id`,`p`.`name`;

-- -----------------------------------------------------
-- View `siete_y_medio`.`total_player_minutes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `siete_y_medio`.`total_player_minutes`;
USE `siete_y_medio`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`adminproyecto`@`%` SQL SECURITY DEFINER VIEW `siete_y_medio`.`total_player_minutes` AS select `rp`.`player_id` AS `player_id`,`p`.`name` AS `name`,sum(timestampdiff(MINUTE,`g`.`start_time`,`g`.`end_time`)) AS `total_minutes_played` from ((`siete_y_medio`.`games` `g` join `siete_y_medio`.`rounds_players` `rp` on((`g`.`game_id` = `rp`.`game_id`))) join `siete_y_medio`.`players` `p` on((`rp`.`player_id` = `p`.`player_id`))) group by `rp`.`player_id`,`p`.`name`;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



-- Alter tables
ALTER TABLE `siete_y_medio`.`players`
DROP INDEX `nombre_UNIQUE`;


-- 1. Eliminar restricciones de claves foráneas
ALTER TABLE `game_players` DROP FOREIGN KEY `fk_Game_has_players_players1`;
ALTER TABLE `rounds` DROP FOREIGN KEY `fk_Rounds_games_players1`;
ALTER TABLE `rounds_players` DROP FOREIGN KEY `fk_Rounds_players_players1`;

-- 2. Modificar la columna en la tabla principal
ALTER TABLE `players` MODIFY `player_id` VARCHAR(45) NOT NULL;

-- 3. Modificar las columnas relacionadas en las tablas foráneas
ALTER TABLE `game_players` MODIFY `player_id` VARCHAR(45) NOT NULL;
ALTER TABLE `rounds` MODIFY `player_id` VARCHAR(45) NOT NULL;
ALTER TABLE `rounds_players` MODIFY `player_id` VARCHAR(45) NOT NULL;

-- 4. Volver a agregar las restricciones de claves foráneas
ALTER TABLE `game_players` 
    ADD CONSTRAINT `fk_Game_has_players_players1`
    FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`);

ALTER TABLE `rounds`
    ADD CONSTRAINT `fk_Rounds_games_players1`
    FOREIGN KEY (`player_id`, `game_id`) REFERENCES `games_players` (`player_id`, `game_id`);

ALTER TABLE `rounds_players`
    ADD CONSTRAINT `fk_Rounds_players_players1`
    FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`);
