use siete_y_medio;


DROP VIEW IF EXISTS info_player;
CREATE VIEW info_player as 
	SELECT r.player_id, p.name, (sum(r.player_start_points)-sum(r.player_end_points)) as "Total Points", count(gp.game_id) as "Total games", DATEDIFF( g.start_time,g.end_time) as "Total minutes" from rounds r
    join game_players gp on r.player_id=gp.player_id
    join players p on gp.player_id=p.player_id
    join games g on gp.game_id=g.game_id
    GROUP BY gp.player_id;
select * from info_player
group by player_id;

-- DROP VIEW If EXISTS informe_ ;
-- CREATE VIEW informe_ AS

DROP VIEW IF EXISTS informe_3 ;
CREATE VIEW informe_3 AS
	SELECT game_id, player_id, min(player_bet) from rounds r
    GROUP BY game_id;

DROP VIEW IF EXISTS informe_9;
CREATE VIEW informe_9 AS
	SELECT game_id, avg(player_bet) from rounds r
    group by game_id
    order by round_number asc limit 1;

DROP VIEW IF EXISTS informe_10;
CREATE VIEW informe_10 AS
	SELECT game_id, avg(player_bet) from rounds r
    group by game_id
    order by round_number desc limit 1;