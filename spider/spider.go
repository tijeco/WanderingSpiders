package spider

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type Spider struct {
	Mass float64
	Cals float64
}

var spiderMassMin = 222.4
var spiderMassMax = 267.4

func MakeSpiders(n int) {
	var wg sync.WaitGroup // number of working goroutines

	// var spiders [n]Spider
	spiders := make([]Spider, n)
	for spiderNum := range spiders {
		wg.Add(n)
		rand.Seed(time.Now().UnixNano())
		num := rand.Float64()
		// num := 0.4771663944913364
		r := spiderMassMin + num*(spiderMassMax-spiderMassMin)
		fmt.Println(r, num)
		go func(spiderNum int) {
			defer wg.Done()

			spiders[spiderNum].Mass = r //+ float64(spiderNum)
		}(spiderNum)

	}
	// spider1.Mass = 10.1
	// spider1.Cals = 10.2
	fmt.Println(spiders)
	// return spiders

}
