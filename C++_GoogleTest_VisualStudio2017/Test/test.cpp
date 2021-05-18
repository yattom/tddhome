#include "pch.h"
#include "../Target/target.h"


TEST(SimpleAssertions, Equality) {
	EXPECT_EQ(42, 42);
}

TEST(SimpleAssertions, True) {
	EXPECT_TRUE(true);
}

// 日本語のテスト名の例。環境で問題が起きたら、削除してください。
// Japanese characters are used for test names.
// If your environment has difficulties to handle them, please delte them.
TEST(シンプルな例, 同じかどうか) {
	EXPECT_EQ(42, 42);
}

TEST(シンプルな例, 真かどうか) {
	EXPECT_TRUE(true);
}


// Test for functions
TEST(Mul2Test, 2_mul2_is_4) {
	EXPECT_EQ(2, mul2(1));
}

TEST(Mul2Test, 0_mul2_is_0) {
	EXPECT_EQ(0, mul2(0));
}

TEST(Mul2Test, Minus_3_mul2_is_minus_6) {
	EXPECT_EQ(-6, mul2(-3));
}


// Test for class objects using test fixture
class CounterTest : public ::testing::Test  {
public:
	Counter sut;
};

TEST_F(CounterTest, Start_from_0) {
	EXPECT_EQ(0, sut.value());
}

TEST_F(CounterTest, Start_up_works) {
	sut.up();
	EXPECT_EQ(1, sut.value());
}

// Test for class objects using test fixture
class CounterUp3Test : public ::testing::Test {
public:
	Counter counter3;

	void SetUp() {
		for (int i = 0; i < 3; i++) {
			counter3.up();
		}
	}
};

TEST_F(CounterUp3Test, Start_up_works_from_3) {
	counter3.up();
	EXPECT_EQ(3 + 1, counter3.value());
}

