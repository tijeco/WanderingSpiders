package spider

import (
	"fmt"
	"math/rand"
	"time"
)

type Spider struct {
	Mass float64
	Cals float64
}

var spiderMassMin = 222.4
var spiderMassMax = 267.4

func MakeSpiders(n int) {

	// var spiders [n]Spider
	spiders := make([]Spider, n)
	for spiderNum := range spiders {
		rand.Seed(time.Now().UnixNano())
		num := rand.Float64()
		// num := 0.4771663944913364
		r := spiderMassMin + num*(spiderMassMax-spiderMassMin)
		fmt.Println(r, num)
		go func(spiderNum int) {

			spiders[spiderNum].Mass = r //+ float64(spiderNum)
		}(spiderNum)

	}
	// spider1.Mass = 10.1
	// spider1.Cals = 10.2
	fmt.Println(spiders)
	// return spiders

}
