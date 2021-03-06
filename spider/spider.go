package spider

import (
	"math/rand"
	"runtime"
	"time"
)

type Spider struct {
	Mass float64
	Cals float64
}

// const (
// 	NGoRoutines = 4
// )

func AddToMap(key string, val Spider, c chan map[string]Spider) {
	mappy := make(map[string]Spider)
	mappy[key] = val
	c <- mappy
}

var spiderMassMin = 222.4
var spiderMassMax = 267.4
var calPerDayMin = 0.0112
var calPerDayMax = 0.1706
var spiderMass, spiderCals, num float64
var spiderID string
var currentSpider Spider

func MakeSpiders(n int, NGoRoutines int) []Spider {
	array := make([]Spider, n)
	c := make(chan int, NGoRoutines)
	runtime.GOMAXPROCS(NGoRoutines)

	chunk := len(array) / NGoRoutines

	for i := 0; i < NGoRoutines; i++ {
		go func(start int) {
			end := start + chunk

			if end > len(array) {
				end = len(array)
			}

			for j := start; j < end; j = j + 1 {
				rand.Seed(time.Now().UnixNano())
				num = rand.Float64()
				spiderMass = spiderMassMin + num*(spiderMassMax-spiderMassMin)
				spiderCals = calPerDayMin + num*(calPerDayMax-calPerDayMin)

				array[j].Mass = spiderMass
				array[j].Cals = spiderCals
			}
			c <- 1
		}(i * chunk)
	}

	// wait for goroutines to finish
	for i := 0; i < NGoRoutines; i++ {
		<-c
	}
	//
	// // var spiders [n]Spider
	// spiders := make([]map[string]Spider, n)
	// c := make(chan map[string]Spider)
	//
	// go func() {
	// 	for spiderNum := 0; spiderNum < n; spiderNum++ {
	// 		rand.Seed(time.Now().UnixNano())
	// 		num = rand.Float64()
	// 		spiderMass = spiderMassMin + num*(spiderMassMax-spiderMassMin)
	// 		spiderCals = calPerDayMin + num*(calPerDayMax-calPerDayMin)
	// 		spiderID = "spider_" + strconv.Itoa(n)
	// 		fmt.Println(spiderID)
	// 		currentSpider = Spider{Mass: spiderMass, Cals: spiderCals}
	// 		AddToMap(spiderID, currentSpider, c)
	// 	}
	// 	close(c)
	//
	// }()
	// for ret := range c {
	// 	spiders = append(spiders, ret)
	// }
	// fmt.Println(spiders)
	return array
}
