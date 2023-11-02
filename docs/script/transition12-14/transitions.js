import { focus } from './focus.js'

export const transition = () =>
  d3.graphviz('#transitions').fade(false).renderDot(dot.description[0].join(''), focus)