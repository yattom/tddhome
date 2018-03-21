#include "pch.h"
#include "../Target/target.h"

TEST(FooTest, FooTest) {
	EXPECT_EQ(2, foo(1));
}

TEST(TestCaseName, TestName) {
  EXPECT_EQ(1, 1);
  EXPECT_TRUE(true);
}