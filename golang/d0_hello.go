package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	inputString, _ := reader.ReadString('\n')
	inputString = strings.Replace(inputString, "\n", "", -1)
	fmt.Println("Hello, World.\n" + inputString)
}
