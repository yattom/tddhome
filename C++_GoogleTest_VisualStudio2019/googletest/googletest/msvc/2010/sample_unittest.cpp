#include "gtest/gtest.h"

#include "sample.h"

TEST(Hello, Say) {
	EXPECT_STREQ(hello(), "Hello, World!\n");

}

class HelloTest : public ::testing::Test {
protected:
	const char* expected = "Hello, World!\n";
	virtual void SetUp() {

	}
};

TEST_F(HelloTest, Say) {
	EXPECT_STREQ(hello(), expected);
}