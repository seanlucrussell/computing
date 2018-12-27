import qualified Data.Set as Set

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

fibonacci :: Int -> Int
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci x = fibonacci (x - 1) + fibonacci (x - 2)

memoized_fib :: Int -> Integer
memoized_fib = (map fib [0 ..] !!)
   where fib 0 = 0
         fib 1 = 1
         fib n = memoized_fib (n-2) + memoized_fib (n-1)
         
cylinderArea :: (RealFloat a) => a -> a -> a
cylinderArea r h = sideArea + 2 * topArea
  where sideArea = 2 * pi * r * h
        topArea = pi * r ^2

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = smallerList ++ [x] ++ biggerList
  where smallerList = quicksort [ a | a <- xs, a <= x ]
        biggerList = quicksort [ a | a <- xs, a > x ]

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)


chain :: (Integral a) => a -> [a]
chain 1 = [1]
chain n
  | even n = n:chain (n `div` 2)
  | odd n = n:chain (n * 3 + 1)

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f x y = f y x

fact :: Int -> Integer
fact = foldl1 (*) . flip take [1..]

data Point = Point Float Float deriving (Show)
data Shape = Circle Point Float | Rectangle Point Point deriving (Show)
c :: Shape
c = Circle (Point 1.0 2.0) 3.0

data Person = Person { first :: String
                     , last :: String
                     } deriving (Show)
