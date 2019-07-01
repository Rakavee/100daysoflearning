package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("Enter Numbers: ")
	r := bufio.NewReader(os.Stdin)
	line, err := r.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	ints, err := parseInts(line)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("ints:", ints)
}

func parseInts(s string) ([]int, error) {
	var (
		fields = strings.Fields(s)
		ints   = make([]int, len(fields))
		err    error
	)
	for i, f := range fields {
		ints[i], err = strconv.Atoi(f)
		if err != nil {
			return nil, err
		}
	}
	return ints, nil
}
