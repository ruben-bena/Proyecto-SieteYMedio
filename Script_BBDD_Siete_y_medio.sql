-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schemasiete_y_medio
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schemasiete_y_medio
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schemasiete_y_medio
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `siete_y_medio`;
CREATE SCHEMA IF NOT EXISTS `siete_y_medio` DEFAULT CHARACTER SET utf8mb4 ;
USE `siete_y_medio` ;

-- -----------------------------------------------------
-- Table `siete_y_medio`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`players` (
  `player_id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `risk_level` INT UNSIGNED NOT NULL,
  `is_ai` BIT(1) NOT NULL,
  PRIMARY KEY (`player_id`),
  UNIQUE INDEX `nombre_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`decks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`decks` (
  `deck_id` VARCHAR(45) NOT NULL,
  `deck_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`deck_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`games` (
  `game_id` INT UNSIGNED NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `deck_id` VARCHAR(45) NOT NULL DEFAULT 'ESP',
  `number_players` INT NOT NULL,
  `number_rounds` INT NOT NULL,
  PRIMARY KEY (`game_id`),
  INDEX `fk_games_decks1_idx` (`deck_id` ASC) VISIBLE,
  CONSTRAINT `fk_games_decks1`
    FOREIGN KEY (`deck_id`)
    REFERENCES `siete_y_medio`.`decks` (`deck_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

	
-- -----------------------------------------------------
-- Table `siete_y_medio`.`game_players`
-- -----------------------------------------------------
CREATE TABLE `siete_y_medio`.`game_players` (
  `game_players_id` VARCHAR(45) NOT NULL,
  `game_id` INT UNSIGNED NOT NULL,
  `player_id` INT UNSIGNED NOT NULL,
  INDEX `fk_game_players_game_idx` (`game_id` ASC),
  INDEX `fk_game_players_player_idx` (`player_id` ASC),
  PRIMARY KEY (`game_players_id`),
  CONSTRAINT `fk_Games_has_players_games1`
    FOREIGN KEY (`game_id`)
    REFERENCES `siete_y_medio`.`games` (`game_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Game_has_players_players1`
    FOREIGN KEY (`player_id`)
    REFERENCES `siete_y_medio`.`players` (`player_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
ALTER TABLE `siete_y_medio`.`game_players`
ADD INDEX `idx_game_id_player_id` (`game_id`, `player_id`);

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
  `player_bet` INT,
  PRIMARY KEY (`round_id`),
  INDEX `fk_Rounds_games_players_idx` (`player_id` ASC, `game_id` ASC) VISIBLE,
  CONSTRAINT `fk_Rounds_games_players1`
    FOREIGN KEY (`player_id` , `game_id`)
    REFERENCES `siete_y_medio`.`game_players` (`game_id` , `player_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siete_y_medio`.`cards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siete_y_medio`.`cards` (
  `card_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `deck_id` VARCHAR(45) NOT NULL,
  `real_value` INT NOT NULL,
  `game_value` INT NOT NULL,
  `priority` INT NULL,
  PRIMARY KEY (`card_id`),
  INDEX `fk_Cards_Decks1_idx` (`deck_id` ASC) VISIBLE,
  CONSTRAINT `fk_Cards_Decks1`
    FOREIGN KEY (`deck_id`)
    REFERENCES `siete_y_medio`.`decks` (`deck_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
