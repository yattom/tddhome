QUnit.module('QUnit の使い方', function () {

    QUnit.module('Hello World', function () {
        QUnit.test('Hello World', function (assert) {
            var actual = "";
            actual = hello();
            assert.equal("Hello, World!", actual);
        })
    });
});

QUnit.module('自動販売機(構造化）', function (hooks) {
    function assert_purchaseable(assert, beverage) {
        vm.get_button(beverage).push();
        assert.equal(vm.take(), beverage);
    }
    function assert_not_purchaseable(assert, beverage) {
        vm.get_button(beverage).push();
        assert.equal(vm.take(), null);
    }
    var vm;
    hooks.beforeEach(function () {
        vm = new VendingMachine();
    });
    QUnit.module('購入できる', function () {
        QUnit.test('ボタンを押さないと、何も出ない', function (assert) {
            var actual = vm.take();
            assert.equal(actual, null);
        });
        QUnit.module('投入金額', function () {
            QUnit.test('100円でコーラが買える', function (assert) {
                vm.insert100();
                assert_purchaseable(assert, "コーラ");
            });
            QUnit.test('200円でレッドブルが買える', function (assert) {
                vm.insert100();
                vm.insert100();
                assert_purchaseable(assert, "レッドブル");
            });
            QUnit.test('100円でレッドブルが買えない', function (assert) {
                vm.insert100();
                assert_not_purchaseable(assert, "レッドブル");
            });
            QUnit.test('0円でコーラが買えない', function (assert) {
                assert_not_purchaseable(assert, "コーラ");
            });
        });
    });
    QUnit.module('選んで購入できる', function (hooks) {
        hooks.beforeEach(function () {
            vm.insert100();
        });
        QUnit.test('ウーロン茶', function (assert) {
            vm.get_button("ウーロン茶").push();
            assert.equal(vm.take(), "ウーロン茶");
        });
        QUnit.test('コーラ', function (assert) {
            vm.get_button("コーラ").push();
            assert.equal(vm.take(), "コーラ");
        });
        QUnit.module('存在しない商品', function () {
            QUnit.test('エリクサーは選べない', function (assert) {
                assert.throws(function () { vm.get_button("エリクサー") });
            });
        });
    });
    QUnit.module('LEDが点灯する', function (hooks) {
        QUnit.test('0円の場合', function(assert) {
            assert.ok(!vm.get_button('コーラ').is_lit());
            assert.ok(!vm.get_button('ウーロン茶').is_lit());
            assert.ok(!vm.get_button('レッドブル').is_lit());
        });
        QUnit.test('100円の場合', function(assert) {
            vm.insert100();
            assert.ok(vm.get_button('コーラ').is_lit());
            assert.ok(vm.get_button('ウーロン茶').is_lit());
            assert.ok(!vm.get_button('レッドブル').is_lit());
        });
        QUnit.test('200円の場合', function(assert) {
            vm.insert100();
            vm.insert100();
            assert.ok(vm.get_button('コーラ').is_lit());
            assert.ok(vm.get_button('ウーロン茶').is_lit());
            assert.ok(vm.get_button('レッドブル').is_lit());
        });
        QUnit.test('300円の場合', function(assert) {
            vm.insert100();
            vm.insert100();
            vm.insert100();
            assert.ok(vm.get_button('コーラ').is_lit());
            assert.ok(vm.get_button('ウーロン茶').is_lit());
            assert.ok(vm.get_button('レッドブル').is_lit());
        });
    });
});


/*
QUnit.module('計算機', function() {
QUnit.module('足し算', function() {
QUnit.test('1+2', function(assert) {
assert.equal(add(1, 2), 3);
});
QUnit.test('3+9', function(assert) {
assert.equal(add(3, 9), 12);
});
});
QUnit.module('引き算', function() {
QUnit.test('2-1', function(assert) {
assert.equal(sub(2, 1), 1);
});
});
});
*/
    // QUnit.module('基礎編', function () {

    //     QUnit.test('assert.ok の使い方', function (assert) {
    //         var truth = true;
    //         assert.ok(truth, 'assert.ok は引数が truthy であるかどうかを検証します');
    //         var falsy = true;
    //         assert.ok(!falsy);
    //     });

    //     // QUnit の assert.equal 系は引数の順番が actual, expected の順(JUnit の逆)なので注意してください
    //     QUnit.test('equal, notEqual の使い方', function (assert) {
    //         assert.equal('hoge', 'hoge');
    //         assert.equal(1, '1', 'equal は == を使います');
    //         assert.notEqual('foo', 'bar');
    //     });

    //     QUnit.test('strictEqual, notStrictEqual の使い方', function (assert) {
    //         assert.strictEqual('1', '1');
    //         assert.notStrictEqual(1, '1', 'strictEqual は === を使います');
    //     });

    //     QUnit.test('deepEqual, notDeepEqual の使い方', function (assert) {
    //         var ary = ['foo', 'bar'];
    //         assert.deepEqual(ary.map(function (str){
    //             return str.toUpperCase();
    //         }), ['FOO', 'BAR'], 'Array の比較を行えます');

    //         var o1 = {name: 'foo', age: 20};
    //         var o2 = {age: 20, name: 'foo'};
    //         assert.deepEqual(o1, o2, 'オブジェクト同士の比較もできます');

    //         var o3 = {name: 'bar', age: 32};
    //         assert.notDeepEqual(o1, o3);
    //     });
    // });


    // QUnit.module('応用編', function () {

    //     QUnit.test('例外のテストの書き方', function (assert) {
    //         assert.throws(function () {
    //             throw new Error('例外');
    //         }, 'throws で例外が投げられることをテストできます');
    //     });

    //     QUnit.test('非同期のテストの書き方', function (assert) {
    //         var done = assert.async();
    //         setTimeout(function () {
    //             assert.equal('hoge', 'hoge', '100ミリ秒後にこの比較が行われています');
    //             done();
    //         }, 100);
    //     });

    // });

