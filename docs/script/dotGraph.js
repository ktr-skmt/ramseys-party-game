import { dot as dot0 } from './turn/dot0.js'
import { dot as dot1 } from './turn/dot1.js'
import { dot as dot10 } from './turn/dot10.js'
import { dot as dot11 } from './turn/dot11.js'
import { dot as dot12 } from './turn/dot12.js'
import { dot as dot13 } from './turn/dot13.js'
import { dot as dot14 } from './turn/dot14.js'
import { dot as dot2 } from './turn/dot2.js'
import { dot as dot3 } from './turn/dot3.js'
import { dot as dot4 } from './turn/dot4.js'
import { dot as dot5 } from './turn/dot5.js'
import { dot as dot6 } from './turn/dot6.js'
import { dot as dot7 } from './turn/dot7.js'
import { dot as dot8 } from './turn/dot8.js'
import { dot as dot9 } from './turn/dot9.js'

const turn0 = []
const turn1 = []
const turn2 = []
const turn3 = []
const turn4 = []
const turn5 = []
const turn6 = []
const turn7 = []
const turn8 = []
const turn9 = []
const turn10 = []
const turn11 = []
const turn12 = []
const turn13 = []
const turn14 = []

dot0.description.forEach(element => turn0.push(element))
dot1.description.forEach(element => turn1.push(element))
dot2.description.forEach(element => turn2.push(element))
dot3.description.forEach(element => turn3.push(element))
dot4.description.forEach(element => turn4.push(element))
dot5.description.forEach(element => turn5.push(element))
dot6.description.forEach(element => turn6.push(element))
dot7.description.forEach(element => turn7.push(element))
dot8.description.forEach(element => turn8.push(element))
dot9.description.forEach(element => turn9.push(element))
dot10.description.forEach(element => turn10.push(element))
dot11.description.forEach(element => turn11.push(element))
dot12.description.forEach(element => turn12.push(element))
dot13.description.forEach(element => turn13.push(element))
dot14.description.forEach(element => turn14.push(element))

const dotGraph = [
  turn0,
  turn1,
  turn2,
  turn3,
  turn4,
  turn5,
  turn6,
  turn7,
  turn8,
  turn9,
  turn10,
  turn11,
  turn12,
  turn13,
  turn14
]

const transform = () => {
  const svg = document.getElementById("graph").getElementsByTagName("svg")[0]
  const g = svg.childNodes[1]
  const tfm = svg.createSVGTransform()
  tfm.setTranslate(25.4, 214)
  g.transform.baseVal.removeItem(2)
  g.transform.baseVal.appendItem(tfm)
  g.id = "sub" + g.id
  Array.from(g.getElementsByTagName("g"))
    .forEach(element => element.id = "sub" + element.id)
}

export const showModal = (turn, i) => {
  document.getElementById("graph").innerHTML = "";
  d3.graphviz("#graph").zoom(false).fade(false).renderDot(dotGraph[turn][i - 1].join(''), transform)
  MicroModal.show('modal-graph')
}