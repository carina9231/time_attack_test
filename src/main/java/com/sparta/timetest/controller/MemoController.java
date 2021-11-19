package com.sparta.timetest.controller;

import com.sparta.timetest.domain.Memo;
import com.sparta.timetest.dto.MemoRequestDto;
import com.sparta.timetest.repository.MemoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class MemoController {

    private final MemoRepository memoRepository;

    @PostMapping("/api/memo")
    public Memo createMemo(@RequestBody MemoRequestDto requestDto) {
        Memo memo = new Memo(requestDto);
        // 응답 보내기
        return memoRepository.save(memo);
    }

    @GetMapping("/api/memo")
    public List<Memo> getMemos() {
        return memoRepository.findAllByOrderByModifiedAtDesc();
    }
}

