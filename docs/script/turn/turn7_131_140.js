import {dot7_131_140} from './dot7_131_140.js';for (let i = 130; i < 140; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_131_140.description[i].join('')); }