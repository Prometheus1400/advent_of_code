package main

import (
	"fmt"
	"strconv"
	"strings"
	"sync"
)

func blink(input []int) []int {
    output := make([]int, 0, len(input))
    for _, num := range input {
        strnum := strconv.Itoa(num)
        if num == 0 {
            output = append(output, 1)
        } else if len(strnum) % 2 == 0 {
            leftHalf, _ := strconv.Atoi(strnum[:len(strnum) / 2])
            righHalf, _ := strconv.Atoi(strnum[len(strnum) / 2:])
            output = append(output, leftHalf) 
            output = append(output, righHalf) 
        } else {
            output = append(output, num * 2024) 
        }
    }
    return output
}

func main() {
    // strInput := "125 17"
    strInput := "2 54 992917 5270417 2514 28561 0 990"
    numBlinks := 75
    strStones := strings.Split(strInput, " ")
    inputNumStones := len(strStones)
    intStones := make([]int, 0, len(strStones)) 
    for _, strval := range strStones {
        intval, _ := strconv.Atoi(strval)
        intStones = append(intStones, intval)
    }
    resultContainer := make(map[int][]int)
    var wg sync.WaitGroup
    var mu sync.Mutex
    for ind, num := range intStones {
        wg.Add(1)
        go func(i int, n int) {
            defer wg.Done()
            stones := []int{n}
            for _ = range numBlinks {
                stones = blink(stones)
            }
            mu.Lock()
            resultContainer[i] = stones
            mu.Unlock()
        }(ind, num)
    }
    wg.Wait()
    fmt.Println(resultContainer)
    output := make([]int, 0, 100)
    for i := range inputNumStones {
        output = append(output, resultContainer[i]...) 
    }

    fmt.Println(len(output))
}
