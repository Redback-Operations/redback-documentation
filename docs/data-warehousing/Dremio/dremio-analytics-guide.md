---
sidebar_position: 3
sidebar_label: Dremio Analytics AFL
---

## **1) Introduction to Dremio**
### **What is Dremio?**
Dremio is a **data lakehouse platform** that enables you to query **data where it lives** without needing to move it into a warehouse. You can connect files, object stores, relational databases, and even NoSQL systems under a **single SQL interface**.
**Key Features:**
*   **Query data in-place** — no ETL pipelines required.
*   **Virtual Datasets (VDS)** — reusable, versionable, shareable SQL views.
*   **Cross-source joins** — combine data across CSV, PostgreSQL, MinIO, etc.
*   **Reflections** — accelerate queries using automatic materializations.
*   **Integration-ready** — works seamlessly with BI tools like Tableau, Power BI, and Superset.
### **Why Use Dremio**
|Traditional Analytics|With Dremio|
|---|---|
|ETL-heavy pipelines|Zero-copy architecture|
|Duplicated data marts|Single, governed source|
|Complex scheduling|Instant dashboards|
|Vendor lock-in|Open formats (Parquet, Iceberg)|
### **Dremio Execution Model**
*   Parses your SQL.
*   Pushes operations **down to sources** (PostgreSQL, S3, etc.) where possible.
*   Executes distributed queries for large datasets.
![](https://beta.appflowy.cloud/api/file_storage/efa01a3a-37f9-4405-8e02-34cb5fa15791/v1/blob/7527f86b%2D88fe%2D495d%2D8140%2Dd222cbb2670c/H250-AOIfLII6qd-WTVzCUYPcc6TuBKv0bh_SdHFYtw=.png)
This guide provides the AFL tutorial using the **Medallion** architecture in Dremio. We’ll model the three layers directly in Dremio Virtual Datasets (VDS) over your PostgreSQL tables:
* **Bronze** = raw access, column naming alignment, no semantic changes
* **Silver** = cleaned & conformed (types, dates, standardised text, light business rules)
* **Gold** = analytics-ready marts for BI (star-like, aggregated/denormalised)
**Source tables (**postgresql_provenance** → ****`public`****):** `afl_games`, `afl_stats`, `afl_players`**Assumed Dremio source name:** `Postgres`**Workspace/Space:** `Analytics`
---
## **2) Dataset Overview — AFL Analytics Data Model**
The AFL dataset is designed to analyse **matches**, **players**, **team performances**, **venues**, and **audience engagement**.
It consists of three primary tables in PostgreSQL (`public.afl_games`, `public.afl_stats`, `public.afl_players`).
We model these in Dremio using the **Medallion Architecture** for scalable analytics.
## **2.1. afl_games** — Match-Level Dataset (Fact Table)
This table captures **match metadata**, weather conditions, scores, and attendance.
|**Column**|**Type**|**Description**|**Example**|**Notes / Data Quality Considerations**|
|---|---|---|---|---|
|`GameId`|VARCHAR|Unique identifier for each game|`AFL2023R15G3`|Primary key; must be unique|
|`Year`|INT|AFL season year|`2023`|Used heavily in partitioning and filtering|
|`Round`|VARCHAR|Fixture round (string)|`Round 15`|Needs trimming; consider standardising as INT|
|`Date`|VARCHAR|Game date (raw string)|`14/07/2023`|Needs parsing to DATE/TIMESTAMP|
|`MaxTemp`|FLOAT|Maximum temperature (°C)|`27.5`|Missing/null for some games|
|`MinTemp`|FLOAT|Minimum temperature (°C)|`13.2`|Missing/null for some games|
|`Rainfall`|FLOAT|Rainfall recorded in mm|`4.5`|Default to 0 when missing|
|`Venue`|VARCHAR|Stadium or ground name|`MCG`|Needs standardisation (e.g., “MCG” vs “Melbourne Cricket Ground”)|
|`StartTime`|VARCHAR|Game start time|`19:40`|Needs parsing into TIME/TIMESTAMP|
|`Attendance`|VARCHAR|Crowd attendance|`85,126`|Stored as string, requires numeric cleanup|
|`HomeTeam`|VARCHAR|Name of home team|`Collingwood`|Requires standardisation (case & spacing)|
|`HomeTeamScoreQT`|FLOAT|Home team’s **quarter-time** score|`24`|Nullable if match abandoned|
|`HomeTeamScoreHT`|FLOAT|Home team’s **half-time** score|`51`|Nullable if match abandoned|
|`HomeTeamScore3QT`|FLOAT|Home team’s **three-quarter-time** score|`74`|Nullable if match abandoned|
|`HomeTeamScoreFT`|FLOAT|Home team’s **full-time** score|`99`|Nullable if match abandoned|
|`HomeTeamScore`|INT|Home team’s final score|`99`|Derived from `HomeTeamScoreFT`|
|`AwayTeam`|VARCHAR|Name of away team|`Carlton`|Requires standardisation|
|`AwayTeamScoreQT`|FLOAT|Away team’s **quarter-time** score|`18`|Nullable if match abandoned|
|`AwayTeamScoreHT`|FLOAT|Away team’s **half-time** score|`39`|Nullable if match abandoned|
|`AwayTeamScore3QT`|FLOAT|Away team’s **three-quarter-time** score|`66`|Nullable if match abandoned|
|`AwayTeamScoreFT`|FLOAT|Away team’s **full-time** score|`88`|Nullable if match abandoned|
|`AwayTeamScore`|INT|Away team’s final score|`88`|Derived from `AwayTeamScoreFT`|
**Grain:** One row per **game**
**Primary Key:** `GameId`
**Usage:**
*   Match results & scoring patterns
*   Venue analysis
*   Weather impact on scoring
*   Attendance prediction
---
## **2.2. afl_stats** — Player Match Statistics (Fact Table)
Captures **player-level statistics** for each match. This is the most granular dataset.
|**Column**|**Type**|**Description**|**Example**|**Notes / Data Quality Considerations**|
|---|---|---|---|---|
|`gameid`|VARCHAR|Foreign key to `afl_games.GameId`|`AFL2023R15G3`|Must always join to `afl_games`|
|`team`|VARCHAR|Team name|`Collingwood`|Requires standardisation|
|`Year`|INT|Season year|`2023`|Filter heavily used|
|`round`|VARCHAR|Fixture round|`Round 15`|Clean to integer where possible|
|`playerid`|INT|Foreign key to `afl_players.PlayerId`|`302`|Join to enrich player bios|
|`displayname`|VARCHAR|Player’s full name|`Nick Daicos`|Use for dashboards|
|`gamenumber`|INT|Player’s game number in the season|`14`|Can be used for career trajectory|
|`disposals`|INT|Total disposals (kicks + handballs)|`29`|Key KPI for midfielders|
|`kicks`|INT|Kicks attempted|`16`|Often used with `handballs`|
|`marks`|INT|Marks taken|`5`|Useful for positional analysis|
|`handballs`|INT|Handballs attempted|`13`|Combined with `kicks` into disposals|
|`goals`|INT|Goals scored|`2`|Forward KPIs|
|`behinds`|INT|Behinds scored|`1`|Goal accuracy metric|
|`hitouts`|INT|Ruck contest wins|`28`|Ruck KPI|
|`tackles`|INT|Tackles laid|`4`|Defensive KPI|
|`inside50s`|INT|Entries inside 50m arc|`6`|Key attacking stat|
|`clearances`|INT|First possession after stoppages|`3`|Midfield KPI|
|`clangers`|INT|Turnovers|`2`|Inverse KPI for efficiency|
|`frees`|INT|Free kicks won|`1`|Combine with `freesagainst`|
|`freesagainst`|INT|Free kicks conceded|`2`|Combine with `frees`|
|`brownlowvotes`|INT|Votes awarded for Brownlow medal|`2`|Predictive analytics use-case|
|`contestedpossessions`|INT|Contested possessions|`14`|Player toughness metric|
|`uncontestedpossessions`|INT|Uncontested possessions|`15`|Player spread/run KPI|
|`goalassists`|INT|Assists resulting in goals|`1`|Offensive effectiveness|
**Grain:** One row per **player per match**
**Foreign Keys:**
*   `gameid` → `afl_games.GameId`
*   `playerid` → `afl_players.PlayerId`**Usage:**
*   Player performance dashboards
*   Season summaries
*   Brownlow prediction
*   Fantasy scoring models
---
## **2.3. afl_players** — Player Profiles (Dimension Table)
Provides **bio and static attributes** for players.
|**Column**|**Type**|**Description**|**Example**|**Notes**|
|---|---|---|---|---|
|`PlayerId`|INT|Unique player identifier|`302`|Primary key|
|`DisplayName`|VARCHAR|Player’s full name|`Nick Daicos`|Used in dashboards|
|`Height`|INT|Height in cm|`185`|Useful for player comparison|
|`Weight`|INT|Weight in kg|`80`|Used in player fitness metrics|
|`Dob`|VARCHAR|Date of birth|`2003-01-03`|Needs parsing to DATE|
|`Position`|VARCHAR|Field position|`Midfielder`|Used for filtering analysis|
|`Origin`|VARCHAR|Junior/feeder club|`Oakleigh Chargers`|Used for AFL draft insights|
**Grain:** One row per player
**Primary Key:** `PlayerId`
**Usage:**
*   Bio enrichment in dashboards
*   Positional performance analysis
*   Age-based KPIs
*   Draft analysis
---
## **2.4. Relationships**
```
afl_games.GameId       1 ──── n   afl_stats.gameid
afl_players.PlayerId   1 ──── n   afl_stats.playerid
```
*   **afl_games** → Central **match fact table**
*   **afl_stats** → Player performance linked to games and players
*   **afl_players** → Dimension table for player bios
---
## **2.5. Data Quality Challenges & Fixes**
|**Issue**|**Impact**|**Resolution Strategy**|
|---|---|---|
|Inconsistent team names|Join mismatches|Apply `UPPER(TRIM(team))` in **Silver** layer|
|Attendance stored as string|BI charting fails|Use regex to strip non-digits|
|Dates stored as VARCHAR|Can't sort timelines|`TRY_CAST` or `TO_DATE()` in **Silver**|
|Null weather values|Skewed scoring/weather models|Fill missing with median or tag as “Unknown”|
|Round stored as VARCHAR|Sorting breaks|Extract numeric using regex|
---
## **2.6. Analytics Opportunities**
### **Game-Level Insights**
*   Scoring patterns per quarter, venue, weather, time of day.
*   Attendance forecasting using historical data + weather.
### **Team-Level Insights**
*   Rolling 5-game form guides.
*   KPI comparison (disposals, goals, tackles).
*   Venue-based advantage modelling.
### **Player-Level Insights**
*   Top performers per season.
*   Brownlow vote prediction models.
*   Fantasy AFL scoring automation.
---
## **2.7. Medallion Layer Mapping**
|**Layer**|**Purpose**|**Example VDS**|**Transformation Focus**|
|---|---|---|---|
|**Bronze**|Raw ingestion|`bronze\_afl\_games`|Column renaming only|
|**Silver**|Cleaned & conformed|`silver\_afl\_stats`|Type casting, normalisation, key creation|
|**Gold**|Curated marts|`gold\_team\_game`|Aggregation, business logic, BI-ready|
---
# **3) Medallion layers**
## 3.1) Bronze Layer (Raw Access & Naming Alignment)
Goal: represent the **raw shape** of data as close to source as possible in Dremio, keeping semantics untouched. We’ll:
* Point at the physical Postgres tables (they are the true Bronze)
* Optionally create **bronze_*** VDS for stable, snake_case columns without type coercion
In Dremio, the Postgres physical tables already serve as Bronze. The optional VDS below gives you stable column names for downstream layers, without changing data types/values.
### 3.1.1 `Analytics.bronze_afl_games`
```sql
CREATE VDS "Analytics"."bronze_afl_games" AS
SELECT
  "GameId"            AS game_id,
  "Year"              AS game_year,
  "Round"             AS round,
  "Date"              AS date_raw,
  "MaxTemp"           AS max_temp_raw,
  "MinTemp"           AS min_temp_raw,
  "Rainfall"          AS rainfall_raw,
  "Venue"             AS venue,
  "StartTime"         AS start_time_raw,
  "Attendance"        AS attendance_raw,
  "HomeTeam"          AS home_team,
  "HomeTeamScoreQT"   AS home_qt_raw,
  "HomeTeamScoreHT"   AS home_ht_raw,
  "HomeTeamScore3QT"  AS home_3qt_raw,
  "HomeTeamScoreFT"   AS home_ft_raw,
  "HomeTeamScore"     AS home_score_raw,
  "AwayTeam"          AS away_team,
  "AwayTeamScoreQT"   AS away_qt_raw,
  "AwayTeamScoreHT"   AS away_ht_raw,
  "AwayTeamScore3QT"  AS away_3qt_raw,
  "AwayTeamScoreFT"   AS away_ft_raw,
  "AwayTeamScore"     AS away_score_raw
FROM "postgresql_provenance"."public"."afl_games";
```
**`bronze_afl_games`** is a raw, column-renamed mirror of the **AFL games** table, preserving all match details (dates, venues, teams, weather, scores, and attendance) for downstream analytics.
### 3.1.2 `Analytics.bronze_afl_stats`
```sql
CREATE VDS "Analytics"."bronze_afl_stats" AS
SELECT
  gameid                AS game_id,
  team,
  "Year"               AS year,
  round,
  playerid              AS player_id,
  displayname           AS player_name_raw,
  gamenumber            AS game_number,
  disposals,
  kicks,
  marks,
  handballs,
  goals,
  behinds,
  hitouts,
  tackles,
  rebounds,
  inside50s,
  clearances,
  clangers,
  frees                 AS frees_for,
  freesagainst          AS frees_against,
  brownlowvotes         AS brownlow_votes,
  contestedpossessions  AS contested_possessions,
  uncontestedpossessions AS uncontested_possessions,
  contestedmarks        AS contested_marks,
  marksinside50         AS marks_inside50,
  onepercenters         AS one_percenters,
  bounces,
  goalassists           AS goal_assists,
  "%Played"            AS pct_played_raw,
  subs
FROM "postgresql_provenance"."public"."afl_stats";
```
**`bronze\_afl\_stats`** is a raw, column-renamed mirror of the **AFL player statistics** table, preserving all per-player, per-game performance metrics (disposals, goals, tackles, clearances, Brownlow votes, etc.) for downstream data cleaning and analytics.
### 3.1.3 `Analytics.bronze_afl_players`
```sql
CREATE VDS "Analytics"."bronze_afl_players" AS
SELECT
  "PlayerId"   AS player_id,
  "DisplayName" AS player_name_raw,
  "Height"     AS height_raw,
  "Weight"     AS weight_raw,
  "Dob"        AS dob_raw,
  "Position"   AS position,
  "Origin"     AS origin
FROM "postgresql_provenance"."public"."afl_players";
```
> Bronze rules of thumb: **no type casting, no semantic fixes**, only column naming and pass-through projection.
## 3.2) Silver Layer (Cleaned, Conformed, Typed)
Goal: standardise types, parse dates/times, normalise text and identifiers so downstream analytics are reliable.
### 3.2.1 `Analytics.silver_afl_games` (typed & parsed)
```sql
CREATE VDS "Analytics"."silver_afl_games" AS
SELECT
  CAST(game_id AS VARCHAR)                           AS game_id,
  CAST(year AS INT)                                  AS year,
  TRIM(CAST(round AS VARCHAR))                       AS round,
  -- Date & Timestamp
  TRY_CAST(date_raw AS DATE)                         AS game_date,
  TRY_CAST(CONCAT(date_raw, ' ', COALESCE(start_time_raw,'00:00')) AS TIMESTAMP) AS game_ts,
  -- Weather
  CAST(max_temp_raw AS FLOAT)                        AS max_temp_c,
  CAST(min_temp_raw AS FLOAT)                        AS min_temp_c,
  CAST(rainfall_raw AS FLOAT)                        AS rainfall_mm,
  TRIM(CAST(venue AS VARCHAR))                       AS venue,
  TRIM(CAST(start_time_raw AS VARCHAR))              AS start_time_str,
  -- Attendance (strip non-digits)
  CAST(REGEXP_REPLACE(COALESCE(attendance_raw,''), '[^0-9]', '') AS INT) AS attendance,
  -- Teams & scores (keep raw quarter splits as floats)
  TRIM(CAST(home_team AS VARCHAR))                   AS home_team,
  CAST(home_qt_raw AS FLOAT)                         AS home_qt,
  CAST(home_ht_raw AS FLOAT)                         AS home_ht,
  CAST(home_3qt_raw AS FLOAT)                        AS home_3qt,
  CAST(home_ft_raw AS FLOAT)                         AS home_ft,
  CAST(home_score_raw AS INT)                        AS home_score,
  TRIM(CAST(away_team AS VARCHAR))                   AS away_team,
  CAST(away_qt_raw AS FLOAT)                         AS away_qt,
  CAST(away_ht_raw AS FLOAT)                         AS away_ht,
  CAST(away_3qt_raw AS FLOAT)                        AS away_3qt,
  CAST(away_ft_raw AS FLOAT)                         AS away_ft,
  CAST(away_score_raw AS INT)                        AS away_score
FROM "Analytics"."bronze_afl_games";
```
### 3.2.2 `Analytics.silver_afl_stats` (typed & conformed)
```sql
CREATE VDS "Analytics"."silver_afl_stats" AS
SELECT
  CAST(game_id AS VARCHAR)                 AS game_id,
  UPPER(TRIM(CAST(team AS VARCHAR)))       AS team,
  CAST(year AS INT)                        AS year,
  TRIM(CAST(round AS VARCHAR))             AS round,
  CAST(player_id AS INT)                   AS player_id,
  TRIM(CAST(player_name_raw AS VARCHAR))   AS player_name,
  CAST(game_number AS INT)                 AS game_number,
  CAST(disposals AS INT)                   AS disposals,
  CAST(kicks AS INT)                       AS kicks,
  CAST(marks AS INT)                       AS marks,
  CAST(handballs AS INT)                   AS handballs,
  CAST(goals AS INT)                       AS goals,
  CAST(behinds AS INT)                     AS behinds,
  CAST(hitouts AS INT)                     AS hitouts,
  CAST(tackles AS INT)                     AS tackles,
  CAST(rebounds AS INT)                    AS rebounds,
  CAST(inside50s AS INT)                   AS inside50s,
  CAST(clearances AS INT)                  AS clearances,
  CAST(clangers AS INT)                    AS clangers,
  CAST(frees_for AS INT)                   AS frees_for,
  CAST(frees_against AS INT)               AS frees_against,
  CAST(brownlow_votes AS INT)              AS brownlow_votes,
  CAST(contested_possessions AS INT)       AS contested_possessions,
  CAST(uncontested_possessions AS INT)     AS uncontested_possessions,
  CAST(contested_marks AS INT)             AS contested_marks,
  CAST(marks_inside50 AS INT)              AS marks_inside50,
  CAST(one_percenters AS INT)              AS one_percenters,
  CAST(bounces AS INT)                     AS bounces,
  CAST(goal_assists AS INT)                AS goal_assists,
  CAST(pct_played_raw AS INT)              AS pct_played,
  TRIM(CAST(subs AS VARCHAR))              AS subs
FROM "Analytics"."bronze_afl_stats";
```
### 3.2.3 `Analytics.silver_afl_players` (typed bios)
```sql
CREATE VDS "Analytics"."silver_afl_players" AS
SELECT
  CAST(player_id AS INT)                    AS player_id,
  TRIM(CAST(player_name_raw AS VARCHAR))    AS player_name,
  CAST(height_raw AS INT)                   AS height_cm,
  CAST(weight_raw AS INT)                   AS weight_kg,
  TRY_CAST(dob_raw AS DATE)                 AS dob,
  TRIM(CAST(dob_raw AS VARCHAR))            AS dob_text,
  UPPER(TRIM(CAST(position AS VARCHAR)))    AS position,
  TRIM(CAST(origin AS VARCHAR))             AS origin
FROM "Analytics"."bronze_afl_players";
```
### 3.2.4 Silver Facts (team-game & player-game)
Aggregate/normalize at canonical grains; still **not** presentation-mart yet.
#### `Analytics.silver_fct_game_team`
```sql
CREATE VDS "Analytics"."silver_fct_game_team" AS
WITH team_game AS (
  SELECT
    s.game_id,
    s.year,
    s.round,
    s.team,
    COUNT(*)                      AS players_count,
    SUM(disposals)                AS team_disposals,
    SUM(kicks)                    AS team_kicks,
    SUM(marks)                    AS team_marks,
    SUM(handballs)                AS team_handballs,
    SUM(goals)                    AS team_goals,
    SUM(behinds)                  AS team_behinds,
    SUM(tackles)                  AS team_tackles,
    SUM(clearances)               AS team_clearances,
    SUM(hitouts)                  AS team_hitouts,
    SUM(inside50s)                AS team_inside50s
  FROM "Analytics"."silver_afl_stats" s
  GROUP BY 1,2,3,4
)
SELECT
  g.game_id,
  g.year,
  g.round,
  g.game_date,
  g.game_ts,
  g.venue,
  g.attendance,
  g.home_team,
  g.away_team,
  CASE WHEN tg.team = g.home_team THEN 'HOME'
       WHEN tg.team = g.away_team THEN 'AWAY'
       ELSE 'OTHER' END           AS side,
  tg.team,
  tg.players_count,
  tg.team_disposals,
  tg.team_kicks,
  tg.team_marks,
  tg.team_handballs,
  tg.team_goals,
  tg.team_behinds,
  tg.team_tackles,
  tg.team_clearances,
  tg.team_hitouts,
  tg.team_inside50s,
  g.home_score,
  g.away_score
FROM "Analytics"."silver_afl_games" g
JOIN team_game tg ON tg.game_id = g.game_id
WHERE tg.team IN (g.home_team, g.away_team);
```
#### `Analytics.silver_fct_player_game`
```sql
CREATE VDS "Analytics"."silver_fct_player_game" AS
SELECT
  s.game_id,
  s.year,
  s.round,
  g.game_date,
  g.venue,
  s.team,
  s.player_id,
  p.player_name,
  p.height_cm,
  p.weight_kg,
  p.position,
  s.disposals,
  s.kicks,
  s.marks,
  s.handballs,
  s.goals,
  s.behinds,
  s.tackles,
  s.clearances,
  s.inside50s,
  s.brownlow_votes,
  s.pct_played
FROM "Analytics"."silver_afl_stats" s
LEFT JOIN "Analytics"."silver_afl_players" p USING (player_id)
LEFT JOIN "Analytics"."silver_afl_games"   g USING (game_id, year, round);
```
### 3.2.5 Silver Dimensions / Helpers
#### `Analytics.silver_dim_game_result`
```sql
CREATE VDS "Analytics"."silver_dim_game_result" AS
SELECT
  game_id,
  year,
  round,
  game_date,
  venue,
  home_team,
  away_team,
  home_score,
  away_score,
  (home_score - away_score)        AS margin,
  CASE WHEN home_score > away_score THEN home_team
       WHEN away_score > home_score THEN away_team
       ELSE 'DRAW' END             AS winner,
  CASE WHEN home_score = away_score THEN 'D'
       WHEN home_score > away_score THEN 'H'
       ELSE 'A' END                AS result_flag
FROM "Analytics"."silver_afl_games";
```
---
## 3.3) Gold Layer (Analytics-Ready Marts)
Goal: publish curated, denormalised views optimised for BI dashboards, with stable measures and dimensions.
### 3.3.1 Team-Game Mart
`Analytics.gold_team_game` (team per game with results, venue, weather, attendance)
```sql
CREATE VDS "Analytics"."gold_team_game" AS
SELECT
  t.*, r.margin, r.winner
FROM "Analytics"."silver_fct_game_team" t
LEFT JOIN "Analytics"."silver_dim_game_result" r USING (game_id);
```
### 3.3.2 Player-Season Leaders
`Analytics.gold_player_season`
```sql
CREATE VDS "Analytics"."gold_player_season" AS
SELECT
  year,
  player_id,
  player_name,
  SUM(disposals)  AS disposals,
  SUM(goals)      AS goals,
  SUM(tackles)    AS tackles,
  SUM(clearances) AS clearances
FROM "Analytics"."silver_fct_player_game"
GROUP BY 1,2,3;
```
### 3.3.3 Attendance & Weather Marts
```sql
CREATE VDS "Analytics"."gold_attendance_by_venue_month" AS
SELECT
  venue,
  DATE_TRUNC('month', game_date) AS month,
  AVG(attendance)                AS avg_attendance,
  COUNT(*)                       AS games
FROM "Analytics"."silver_afl_games"
WHERE game_date IS NOT NULL AND attendance IS NOT NULL
GROUP BY 1,2;

CREATE VDS "Analytics"."gold_weather_vs_scoring" AS
SELECT
  year,
  venue,
  rainfall_mm,
  max_temp_c,
  min_temp_c,
  (home_score + away_score) AS total_points
FROM "Analytics"."silver_afl_games"
WHERE rainfall_mm IS NOT NULL OR max_temp_c IS NOT NULL;
```
### 3.3.4 Time-Series & Windows (Gold Helpers)
```sql
CREATE VDS "Analytics"."gold_monthly_scoring_trend" AS
SELECT
  DATE_TRUNC('month', game_date) AS month,
  AVG(home_score + away_score)   AS avg_total_points
FROM "Analytics"."silver_afl_games"
WHERE game_date IS NOT NULL
GROUP BY 1
ORDER BY 1;

CREATE VDS "Analytics"."gold_team_form_last5" AS
WITH base AS (
  SELECT game_id, year, round, game_date, home_team AS team,
         CASE WHEN home_score > away_score THEN 1 WHEN home_score < away_score THEN 0 ELSE 0.5 END AS win_flag
  FROM "Analytics"."silver_afl_games"
  UNION ALL
  SELECT game_id, year, round, game_date, away_team AS team,
         CASE WHEN away_score > home_score THEN 1 WHEN away_score < home_score THEN 0 ELSE 0.5 END AS win_flag
  FROM "Analytics"."silver_afl_games"
)
SELECT *,
  AVG(win_flag) OVER (
    PARTITION BY team
    ORDER BY game_date
    ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
  ) AS last5_win_rate
FROM base;

CREATE VDS "Analytics"."gold_player_rolling3" AS
SELECT
  player_id,
  player_name,
  team,
  game_date,
  disposals,
  goals,
  AVG(disposals) OVER (
    PARTITION BY player_id
    ORDER BY game_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS avg_disposals_last3,
  AVG(goals) OVER (
    PARTITION BY player_id
    ORDER BY game_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS avg_goals_last3
FROM "Analytics"."silver_fct_player_game"
WHERE game_date IS NOT NULL;
```
---
## 4) Performance & Governance
### Reflections (where they help most)
* **Silver:**
	* _Raw reflections_ on `silver_afl_stats` (large, frequently aggregated).
	* _Raw_ on `silver_afl_games` for heavy filters by season/venue.
* **Gold:**
	* _Aggregation reflections_ on `gold_team_game` with dims (`team`,`year`,`venue`) and measures (`team_goals`,`team_disposals`, etc.).
### Pushdown & Pruning
* Filter by `year`/`team` **upstream** (Silver) to reduce scanned rows in Postgres.
* Project only required columns in Silver Facts.
### Naming & Docs
* Prefix by layer: `bronze_*`, `silver_*`, `gold_*`.
* Add a header comment in each VDS: purpose, grain, owners, refresh/lineage notes.
---
## 5) Troubleshooting Quick Hits
* **Type errors** → verify Silver casts; for dates use `TO_DATE(dob_text, 'DD/MM/YYYY')` if needed.
* **Duplicate rows** → aggregate `silver_afl_stats` to team-game **before** joining to games.
* **Mismatched team strings** → standardise in Silver (`UPPER(TRIM(team))`).
* **Slow dashboards** → add Gold aggregation reflections, check **Job Profile**.
---
## 6) What Goes Where (Cheat Sheet)
* **Bronze**: mirrors Postgres, stable names only → `bronze_afl_*`
* **Silver**: typed, parsed, conformed; canonical facts/dims → `silver_afl_*`, `silver_fct_*`, `silver_dim_*`
* **Gold**: business-ready marts for BI; time-series & window helpers → `gold_*`
You now have a clean **Bronze ▸ Silver ▸ Gold** flow for AFL analytics in Dremio. Connect your BI tool directly to **Gold** and iterate fast while keeping lineage and quality under control.
---
## **7) Reflections for Performance**
Reflections **materialize results** for heavy joins/aggregations:
*   Use **Raw Reflections** → speed up queries over large staging tables.
*   Use **Aggregation Reflections** → pre-summarize metrics for dashboards.
**When to add a reflection:**
*   Query scans > 500MB frequently.
*   Aggregations repeated across dashboards.
---
## **8) Security & Governance Best Practices**
*   **Mask PII** before exposing data:LEFT(customer_unique_id, 6) AS anonymized_id
*   **Restrict access**: give BI users read-only permissions on curated spaces.
*   Always **document transformations** using `\-\- comments`.
---
## **9) Summary Table of Do’s & Don’ts**
|✅ **Do**|❌ **Don’t**|
|---|---|
|Cast once in staging VDS|Repeat CASTs everywhere|
|Use clear naming standards|Use ambiguous names|
|Filter early|Fetch full datasets blindly|
|Normalize join keys|Join uncleaned columns|
|Use CAST for fragile data|Hard CAST on raw timestamps|
|Document every VDS|Leave “magic numbers” unexplained|
|Use reflections for hot dashboards|Scan CSVs repeatedly|
---
# **10) Troubleshooting Common Issues in Dremio**
Even with best practices, issues arise.
This section covers **frequent problems**, **why they happen**, and **how to fix them**.
## **10.1 “Table Not Found” Errors**
**Why it happens:**
*   Path not quoted properly.
*   Dataset promoted in the wrong source.
*   Dataset renamed/moved.
**Fix:**
*   Always quote full path:SELECT *
FROM "@jrees"."E-Commerce Sales Dataset"."olist_orders_dataset";
*   Double-check dataset under **Sources**.
## **10.2 Wrong Data Types**
**Symptom:** Numeric columns show as text, timestamps as strings.
**Fix:**
Always cast in **staging VDS**:
```
CAST(price AS DOUBLE) AS price,
CAST(order_purchase_timestamp AS TIMESTAMP) AS order_ts
```
**Example of detecting unexpected types:**
```
SELECT DISTINCT typeof(order_purchase_timestamp)
FROM "@jrees"."E-Commerce Sales Dataset"."olist_orders_dataset";
```
## **10.3 Date Parsing Errors**
**Problem:** Invalid date formats crash `CAST`.
**Solution:** Use `CAST` or `TO_DATE`:
```
CAST(order_purchase_timestamp AS TIMESTAMP)
-- OR for custom format:
TO_DATE(order_purchase_timestamp, 'DD/MM/YYYY')
```
## **10.4 Duplicate Rows After Joins**
**Why:** Multiple matches per key on either side.
**Fix:** Deduplicate using `ROW_NUMBER()`:
```
WITH dedup_products AS (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY updated_at DESC) AS rn
  FROM products_raw
)
SELECT * FROM dedup_products WHERE rn = 1;
```
## **10.5 Slow Queries**
### **Symptoms**
*   Job takes >60 seconds.
*   Scans millions of rows unnecessarily.
### **Fixes**
#### **1) Filter Early**
```
SELECT *
FROM "Analytics"."stg_orders"
WHERE order_purchase_ts >= CURRENT_DATE - INTERVAL '30' DAY;
```
#### **2) Use Parquet Over CSV**
*   Convert CSVs → Parquet for faster scans.
#### **3) Add Reflections**
*   Use **aggregation reflections** for heavy dashboards.
#### **4) Avoid Wide SELECTs**
```
-- Bad 
SELECT *
-- Good 
SELECT order_id, price, freight_value
```
## **10.6 Cross-Source Joins Are Too Slow**
**Problem:** Joining Postgres + CSV + S3 simultaneously causes shuffles.
**Solution:**
*   Pre-filter each side before joining.
*   Materialize one dataset as a **raw reflection**.
*   Join **small selective tables** to **large fact tables**, not the other way.
## **10.7 “Out of Memory” (OOM) Failures**
*   Reduce columns and rows scanned.
*   Use **incremental reflections** on partitioned datasets.
*   Push heavy aggregations down to the source when supported.
## **10.8 Debugging via Job Profile**
Use Dremio’s **Job Profile**:
*   Check **Scanned Bytes** → indicates where to optimize filters.
*   Look at **Join Types** → “Broadcast” vs “Hash” joins.
*   See if **Pushdowns** are applied.
## **10.9 Checklist Before Escalation**
Before escalating a query issue:
*   Are filters applied at staging level?
*   Are join keys cleaned, trimmed, and typed?
*   Is CSV converted to Parquet?
*   Can a reflection accelerate this VDS?
