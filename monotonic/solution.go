// NOTE: I've written this code without any prior Go experience whatsoever, so
// there is most likely plenty of room for improvement. I didn't write code in
// Go in the real interview :p

package main

func isMonotonic(list []int) bool {
	n := len(list)
	if n <= 2 {
		return true
	} else {
		diff := make([]int, n-1)
		for i := 0; i < n-1; i++ {
			diff[i] = list[i+1] - list[i]
		}

		flag1, flag2 := true, true
		for i := 0; i < n-1; i++ {
			flag1 = flag1 && diff[i] <= 0
			flag2 = flag2 && diff[i] >= 0
		}

		return flag1 || flag2
	}
}

func assert(v bool) {
	if !v {
		panic("Assertion failed")
	}
}

func main() {
	assert(isMonotonic([]int{}))
	assert(isMonotonic([]int{0}))
	assert(isMonotonic([]int{1, 2, 3, 4}))
	assert(isMonotonic([]int{4, 3, 2, 1}))
	assert(isMonotonic([]int{0, 0, 0, 0}))
	assert(!isMonotonic([]int{1, 2, 1, 2}))
}
