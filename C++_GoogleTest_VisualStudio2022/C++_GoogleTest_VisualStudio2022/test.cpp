#include "pch.h"
#include "fizzbuzz.h"

TEST(TestCaseName, TestName) {
  EXPECT_EQ(1, 1);
  EXPECT_TRUE(true);
}

TEST(FizzBuzz, 1ÇÃèÍçáÇÕÇªÇÃÇ‹Ç‹) {
	EXPECT_EQ("1", fizzbuzz(1));
}

TEST(FizzBuzz, 2ÇÃèÍçáÇÕÇªÇÃÇ‹Ç‹) {
	EXPECT_EQ("2", fizzbuzz(2));
}

TEST(FizzBuzz, 3ÇÃèÍçáÇÕFizz) {
	EXPECT_EQ("Fizz", fizzbuzz(3));
}



