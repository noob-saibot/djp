/* D3 Tree */
/* Copyright 2013 Peter Cook (@prcweb); Licensed MIT */

// Tree configuration
var branches = [];
var seed = {i: 0, x: 420, y: 600, a: 0, l: 130, d:0}; // a = angle, l = length, d = depth
var da = 0.4; // Angle delta
var dl = 0.82; // Length delta (factor)
var ar = 0.7; // Randomness
var maxDepth = 3;


// Tree creation functions
function branch(b) {
	var end = endPt(b), daR, newB;

	branches.push(b);

	if (b.d === maxDepth)
		return;

	// Left branch
	daR = ar * Math.random() - ar * 0.5;
	newB = {
		i: branches.length,
		x: end.x,
		y: end.y,
		a: b.a - da + daR,
		l: b.l * dl,
		d: b.d + 1,
		parent: b.i
	};
	branch(newB);

	// Right branch
	daR = ar * Math.random() - ar * 0.5;
	newB = {
		i: branches.length,
		x: end.x, 
		y: end.y, 
		a: b.a + da + daR, 
		l: b.l * dl, 
		d: b.d + 1,
		parent: b.i
	};
	branch(newB);
}

function regenerate(initialise) {
	branches = [];
	branch(seed);
	initialise ? create() : update();
}

function endPt(b) {
	// Return endpoint of branch
	var x = b.x + b.l * Math.sin( b.a );
	var y = b.y - b.l * Math.cos( b.a );
	return {x: x, y: y};
}


// D3 functions
function x1(d) {return d.x;}
function y1(d) {return d.y;}
function x2(d) {return endPt(d).x;}
function y2(d) {return endPt(d).y;}
function highlightParents(d) {
	var colour = d3.event.type === 'mouseover' ? '#2f4f4f' : '#837da2';
	var depth = d.d;
	for(var i = 0; i <= depth; i++) {
		d3.select('#id-'+parseInt(d.i)).style('stroke', colour);
		d = branches[d.parent];
	}	
}

function create() {
	d3.select('svg')
		.selectAll('line')
		.data(branches)
		.enter()
		.append('line')
		.attr('x1', x1)
		.attr('y1', y1)
		.attr('x2', x2)
		.attr('y2', y2)
		.style('stroke-width', function(d) {return parseInt(maxDepth + 10 - d.d) + 'px';})
		.style('stroke-linecap','round')
		.attr('id', function(d) {return 'id-'+d.i;})
		.on('mouseover', highlightParents)
		.on('mouseout', highlightParents);
}

function create_by_user(place) {
	d3.select('svg')
		.selectAll('line')
		.data(place)
		.enter()
		.append('line')
		.attr('x1', x1)
		.attr('y1', y1)
		.attr('x2', x2)
		.attr('y2', y2)
		.style('stroke-width', function(d) {return parseInt(maxDepth + 10 - d.d) + 'px';})
		.style('stroke-linecap','round')
		.attr('id', function(d) {return 'id-'+d.i;})
		.on('mouseover', highlightParents)
		.on('mouseout', highlightParents);
}

function update() {
	d3.select('svg')
		.selectAll('line')
		.data(branches)
		.transition()
		.attr('x1', x1)
		.attr('y1', y1)
		.attr('x2', x2)
		.attr('y2', y2);

	var colour = d3.event.type === 'mouseover' ? '#2f4f4f' : '#837da2';

	d3.select('svg')
		.selectAll('line')
		.style('stroke', colour);
	test(maxDepth);
}

function test(depth) {

	d3.selection.prototype.moveToFront = function() {  
      return this.each(function(){
        this.parentNode.appendChild(this);
      });
    };

	var random_list = [];
	for(var j = 0; j < branches.length; j++)
	{
		if (branches[j].d == maxDepth)
		{
			random_list.push(branches[j].i)
		}
	}
	var d = random_list[Math.floor(Math.random()*random_list.length)]
	for(var i = 0; i <= maxDepth; i++)
	{
		//d3.select('#id-'+d).remove()
		//create_by_user(branches[d])
		d3.select('#id-'+d)
						.style('stroke', 'green')
						.moveToFront();
		d = branches[d].parent
	}
	
}

d3.selectAll('.regenerate')
	.on('click', regenerate);

regenerate(true);
test(maxDepth);
console.log(branches[10])
