#include "pch.h"
#include "Range.h"

namespace ������ԃI�u�W�F�N�g {

	TEST(�I�u�W�F�N�g����, ���[�_�Ə�[�_������) {
		Range sut = Range(3, 8);
		const auto lower = sut.getLower();
		const auto upper = sut.getUpper();
		EXPECT_EQ(3, lower);
		EXPECT_EQ(8, upper);
	}

	TEST(�I�u�W�F�N�g����, �r���_�[���ۂ�����������) {
		Range sut = RangeBuilder().lower(3).upper(8).build();
		const auto lower = sut.getLower();
		const auto upper = sut.getUpper();
		EXPECT_EQ(3, lower);
		EXPECT_EQ(8, upper);
	}
	TEST(�I�u�W�F�N�g����, �s��_��[�_��艺�[�_���傫����Ԃ���邱�Ƃ͂ł��Ȃ�) {
		EXPECT_THROW(Range(8, 3), std::invalid_argument);
	}

	TEST(������\��, 3��8�̏ꍇ) {
		Range sut = RangeBuilder().lower(3).upper(8).build();
		EXPECT_EQ("[3,8]", sut.toString());
	}

	TEST(������\��, �}�C�i�X2��10�̏ꍇ) {
		Range sut = RangeBuilder().lower(-2).upper(10).build();
		EXPECT_EQ("[-2,10]", sut.toString());
	}

	TEST(�ʂ̕�Ԃ����S�Ɋ܂ނ��ǂ����𔻒�ł���, ���[�_���܂�) {
		Range r3_8 = RangeBuilder().lower(3).upper(8).build();
		Range r4_5 = RangeBuilder().lower(4).upper(5).build();
		EXPECT_TRUE(r3_8.contains(r4_5));
	}

	TEST(�ʂ̕�Ԃ����S�Ɋ܂ނ��ǂ����𔻒�ł���, �ԗ��I�ȃe�X�g) {
		// this(L--U)�ɑ΂���other(l--u)���ǂ��Ɉʒu���邩�̃p�^�[��
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