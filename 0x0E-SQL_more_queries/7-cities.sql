- script that creates the database and table cities on mySQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
       state_id INT NOT NULL,
        FOREIGN KEY(state_id) REFRENCES states(id),
       name VARCHAR(256) NOT NULL);
