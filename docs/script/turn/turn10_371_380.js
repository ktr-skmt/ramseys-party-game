import {dot10_371_380} from './dot10_371_380.js';for (let i = 370; i < 380; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_371_380.description[i].join('')); }