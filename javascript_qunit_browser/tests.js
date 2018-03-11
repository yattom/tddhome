
class RPG {
  constructor() {
  }

  setPlayer(player) {
    this.player = player
    this.attacker = player
  }

  setMonster(monster) {
    this.monster = monster
    this.defender = monster
  }

  attack(){
    this.lastMessage = this.attacker.name + "が" + this.defender.name + "を攻撃した"
    var temp = this.attacker
    this.attacker = this.defender
    this.defender = temp
  }

  getLastMessage() {
    return this.lastMessage
  }
}

class Player {
  constructor() {
    this.name = "プレイヤー"
  }
}
class Monster {
  constructor() {
    this.name = "モンスター"
  }
}

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
  var game = new RPG();
  game.setPlayer(new Player());
  game.setMonster(new Monster());
  game.attack();
  game.attack();
  var msg = game.getLastMessage();
  assert.equal( msg, "モンスターがプレイヤーを攻撃した" );
});
