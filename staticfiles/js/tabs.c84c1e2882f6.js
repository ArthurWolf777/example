"use strict";

(function(d) {
    let tabstext = Array.prototype.slice.apply(d.querySelectorAll('.tab-text'));
    let tab = Array.prototype.slice.apply(d.querySelectorAll('.tab'));

    d.getElementById('tabs-menu').addEventListener('click', e => {
        if (e.target.tagName == 'LI'){
            let index =  tabstext.indexOf(e.target);
            console.info(index);

            tabstext.map(tabstext => tabstext.classList.remove('active'));
            tabstext[index].classList.add('active');

            tab.map(tab => tab.classList.remove('active'));
            tab[index].classList.add('active');
        }
    });
})(document);