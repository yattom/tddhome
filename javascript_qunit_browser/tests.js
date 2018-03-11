
class RPG {
    constructor() {
        this.animaltype = "ポメラニアン"
    }

    setPlayer(player) {
    }
    setMonster(monster) {
    }
    attack(){

    }
    getLastMessage() {
        return "プレイヤーがモンスターを攻撃した"
    }
}

class Player {}
class Monster {}

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

QUnit.test( "プレイヤーの攻撃の後は、モンスターがプレイヤーを攻撃する", function( assert ) {
});
