import {dot9_71_80} from './dot9_71_80.js';for (let i = 0; i < 10; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_71_80.description[i].join('')); }