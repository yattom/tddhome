#include "pch.h"
#include "Range.h"

namespace 整数閉区間オブジェクト {

	TEST(オブジェクト生成, 下端点と上端点を持つ) {
		Range sut = Range(3, 8);
		const auto lower = sut.getLower();
		const auto upper = sut.getUpper();
		EXPECT_EQ(3, lower);
		EXPECT_EQ(8, upper);
	}

	TEST(オブジェクト生成, ビルダーっぽく初期化する) {
		Range sut = RangeBuilder().lower(3).upper(8).build();
		const auto lower = sut.getLower();
		const auto upper = sut.getUpper();
		EXPECT_EQ(3, lower);
		EXPECT_EQ(8, upper);
	}
	TEST(オブジェクト生成, 不正_上端点より下端点が大きい閉区間を作ることはできない) {
		EXPECT_THROW(Range(8, 3), std::invalid_argument);
	}

	TEST(文字列表現, 3と8の場合) {
		Range sut = RangeBuilder().lower(3).upper(8).build();
		EXPECT_EQ("[3,8]", sut.toString());
	}

	TEST(文字列表現, マイナス2と10の場合) {
		Range sut = RangeBuilder().lower(-2).upper(10).build();
		EXPECT_EQ("[-2,10]", sut.toString());
	}

	TEST(別の閉区間を完全に含むかどうかを判定できる, 両端点を含む) {
		Range r3_8 = RangeBuilder().lower(3).upper(8).build();
		Range r4_5 = RangeBuilder().lower(4).upper(5).build();
		EXPECT_TRUE(r3_8.contains(r4_5));
	}

	TEST(別の閉区間を完全に含むかどうかを判定できる, 網羅的なテスト) {
		// this(L--U)に対してother(l--u)がどこに位置するかのパターン
		// .....L------U....
		// l--u.:......:....
		// l----u......:....
		// l----=---u..:....
		// l----=------u....
		// l----=------=---u
		// .....l---u..:....
		// .....l------u....
		// .....:..l---u....
		// .....:..l---=---u
		// .....:......l---u
		// .....:......:.l-u
		Range r3_8 = RangeBuilder().lower(3).upper(8).build();
		EXPECT_FALSE(r3_8.contains(Range(1, 2)));
		EXPECT_FALSE(r3_8.contains(Range(1, 3)));
		EXPECT_FALSE(r3_8.contains(Range(1, 5)));
		EXPECT_FALSE(r3_8.contains(Range(1, 8)));
		EXPECT_FALSE(r3_8.contains(Range(1, 10)));
		EXPECT_TRUE(r3_8.contains(Range(3, 5)));
		EXPECT_TRUE(r3_8.contains(Range(3, 8)));
		EXPECT_TRUE(r3_8.contains(Range(5, 8)));
		EXPECT_FALSE(r3_8.contains(Range(5, 10)));
		EXPECT_FALSE(r3_8.contains(Range(8, 10)));
		EXPECT_FALSE(r3_8.contains(Range(9, 10)));
	}
}