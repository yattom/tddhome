using Microsoft.VisualStudio.TestPlatform.ObjectModel.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace csharp_mstest_test
{
    [TestClass]
    public class ClosedRangeTest
    {
        [TestMethod]
        public void _3_8で作成できる()
        {
            // Arrange
            var sut = new ClosedRange(3, 8);

            // Act & Assert
            Assert.AreEqual(3, sut.getLower());
            Assert.AreEqual(8, sut.getUpper());
        }

        [TestMethod]
        public void _マイナス5_0で作成できる()
        {
            // Arrange
            var sut = new ClosedRange(-5, 0);

            // Act & Assert
            Assert.AreEqual(-5, sut.getLower());
            Assert.AreEqual(0, sut.getUpper());
        }

        [TestMethod]
        public void 上端点より下端点が大きい閉区間を作ると例外が発生する_8_3の場合()
        {
            Assert.ThrowsException<ArgumentException>(() => new ClosedRange(8, 3));
        }

        [TestMethod]
        public void 上端点より下端点が大きい閉区間を作ると例外が発生する_5_4の場合()
        {
            Assert.ThrowsException<ArgumentException>(() => new ClosedRange(5, 4));
        }

        [TestMethod]
        public void 上端点と端点が等しい閉区間は作れる()
        {
            new ClosedRange(5, 5);
            Assert.IsTrue(true, "例外が起きない");
        }

        [DataTestMethod]
        [DataRow(3, 8, "[3,8]")]
        [DataRow(-5, 0, "[-5,0]")]
        public void ToStringのテスト(int lower, int upper, string expected)
        {
            // Arrange
            var sut = new ClosedRange(lower, upper);

            // Act
            var actual = sut.ToString();

            // Assert
            Assert.AreEqual(expected, actual);
        }

        [DataTestMethod]
        [DataRow(3, true, "下端点と等しい")]
        [DataRow(8, true, "上端点と等しい")]
        [DataRow(4, true, "下端と上端の間")]
        [DataRow(2, false, "下端点より小さい")]
        [DataRow(9, false, "上端点より大きい")]
        public void 指定した整数を含むかどうかを判定できる(int point, bool expected, string label)
        {
            // Arrange
            var sut = new ClosedRange(3, 8);

            // Act & Assert
            Assert.AreEqual(expected, sut.contains(point));
        }

        [TestMethod]
        public void 指定した区間を含むかどうかを判定できる()
        {
            var sut = new ClosedRange(3, 8);
            /*
             *     3    8
             *     +----+
             *      +--+     == (4,7)   ==> true
             *  +-+          == (0,2)   ==> false
             *           +-+ == (9,10)  ==> false
             *    +--+       == (2,5)   ==> false
             *         +--+  == (7,10)   ==> false
             *  +--------+   == (1,9)   ==> false
             *     +----+    == (3,8)   ==> true
             */
            Assert.IsTrue(sut.contains(new ClosedRange(4, 7)));
            Assert.IsFalse(sut.contains(new ClosedRange(0, 2)));
            Assert.IsFalse(sut.contains(new ClosedRange(9, 10)));
            Assert.IsFalse(sut.contains(new ClosedRange(2, 5)));
            Assert.IsFalse(sut.contains(new ClosedRange(7, 10)));
            Assert.IsFalse(sut.contains(new ClosedRange(1, 9)));
            Assert.IsTrue(sut.contains(new ClosedRange(3, 8)));
        }
    }
}
