QUnit.test( "hello test", function( assert ) {
  assert.ok( 1 == "1", "Passed!" );
});

QUnit.test( "プレイヤーがモンスターを攻撃する", function( assert ) {
  var game = new RPG();
  game.setPlayer(new Player());
  game.setMonster(new Monster());
  game.attack();
  var msg = game.getLastMessage();
  assert.ok( msg == "プレイヤーがモンスターを攻撃した", "Passed!" );
});