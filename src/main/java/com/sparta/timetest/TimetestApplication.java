package com.sparta.timetest;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@EnableJpaAuditing
@SpringBootApplication
public class TimetestApplication {

    public static void main(String[] args) {
        SpringApplication.run(TimetestApplication.class, args);
    }
}
