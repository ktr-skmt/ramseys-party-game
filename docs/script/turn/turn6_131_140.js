import {dot6_131_140} from './dot6_131_140.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot6_131_140.description[i].join('')); }