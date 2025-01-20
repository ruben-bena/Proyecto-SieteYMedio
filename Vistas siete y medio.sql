use siete_y_medio;
CREATE OR REPLACE VIEW `player_statistics` AS
SELECT 
    p.player_id, p.name AS `player_name`, SUM(rp.player_end_points - rp.player_start_points) AS total_points_gained, COUNT(DISTINCT rp.game_id) AS `games_played`,
    SUM(TIMESTAMPDIFF(MINUTE, g.start_time, g.end_time)) AS `total_minutes_played`
FROM `players` p
JOIN `rounds_players` rp ON p.player_id=rp.player_id
JOIN `games` g ON rp.game_id=g.game_id
GROUP BY p.player_id, p.name;
select * from player_statistics;

# INFORMES --------------------------------------------
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
#Incompleto

CREATE OR REPLACE VIEW informe_1 as
	SELECT 
		p.player_id AS identificador_jugador,
		SUBSTRING_INDEX(c.name, ' ', 1) AS palo_carta_inicial_mas_repetida,
		SUBSTRING_INDEX(c.name, ' ', -1) AS carta_inicial_mas_repetida,
		COUNT(rp.first_cart_in_hand) AS numero_veces_repetida,
		COUNT(DISTINCT rp.game_id) AS total_partidas_jugadas
	FROM 
		siete_y_medio.players p
	JOIN 
		siete_y_medio.rounds_players rp ON p.player_id = rp.player_id
	JOIN 
		siete_y_medio.cards c ON rp.first_cart_in_hand = c.card_id
	GROUP BY 
		p.player_id, rp.first_cart_in_hand
	ORDER BY 
		p.player_id, numero_veces_repetida DESC;
    select * from informe_1;
    
CREATE OR REPLACE VIEW informe_2 AS
	SELECT game_id, player_id, max(player_bet) from rounds_players r
    GROUP BY game_id;
select * from informe_2;


CREATE OR REPLACE VIEW informe_3 AS
	SELECT game_id, player_id, min(player_bet) FROM rounds_players r
    GROUP BY game_id;
select * from informe_3;

CREATE OR REPLACE VIEW informe_5 AS 
    SELECT game_id, puntos_ganados
	FROM (
		SELECT rp.game_id, rp.player_id, MAX(rp.player_end_points - rp.player_start_points) AS puntos_ganados
		FROM siete_y_medio.rounds_players rp
		JOIN siete_y_medio.players p ON rp.player_id = p.player_id
		GROUP BY rp.game_id
	) AS ganadores
	JOIN siete_y_medio.players p ON ganadores.player_id = p.player_id
	WHERE p.is_ai = 1;
select * from informe_5;

CREATE OR REPLACE VIEW informe_6 AS
	SELECT rp.game_id AS game_id, COUNT(CASE WHEN rp.player_bank=1 AND rp.player_end_points > rp.player_start_points THEN 1 END ) AS bank_wins 
	FROM rounds_players rp
	GROUP BY rp.game_id;
select * from informe_6;

CREATE OR REPLACE VIEW informe_7 AS
	select game_id, count(player_bank) from rounds_players
    group by game_id;
select * from informe_7;


CREATE OR REPLACE VIEW informe_8 AS
	select game_id, avg(player_bet) from rounds_players r
    group by game_id;
select * from informe_8;
    
CREATE OR REPLACE VIEW informe_9 AS
	SELECT game_id, avg(player_bet) from rounds_players r
    where round_number=1
    group by game_id;
select * from informe_9;

CREATE OR REPLACE VIEW informe_10 AS
	SELECT game_id, avg(player_bet) from rounds_players r
	where round_number in (select max(r.round_number) from rounds_players r group by game_id)
    group by game_id;
select * from informe_10;
    



