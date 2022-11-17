# LiFep
LiFep (Lisp Interpreter For Educational Purposes) 

With inspiration from https://github.com/kanaka/mal
 
# Features
- Support for basic atoms (Booleans, Nil, Integers)
- Support for Globally scoped definitions with `def!` and Local definitions with `let*`
- Support for `if` and `do`
- Support for custom functions with `fn*`

# Examples
### Fibonacci
`(def! fib (fn* (N) (if (= N 0) 1 (if (= N 1) 1 (+ (fib (- N 1)) (fib (- N 2)))))))`

`(fib 10)`
