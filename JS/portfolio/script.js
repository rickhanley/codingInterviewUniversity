import * as THREE from 'three';
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader';
import { TextGeometry } from 'three/examples/jsm/geometries/TextGeometry';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const fontLoader = new FontLoader();
fontLoader.load('path-to-your-font.json', (font) => {
    const textGeometry = new TextGeometry('My Portfolio', {
        font: font,
        size: 1,
        height: 0.5,
    });

    const textMaterial = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const textMesh = new THREE.Mesh(textGeometry, textMaterial);

    textMesh.position.z = -10; // Place into the screen
    textMesh.rotation.x = Math.PI / 8; // Tilt slightly
    textMesh.rotation.y = Math.PI / 8; // Angle slightly

    scene.add(textMesh);
});

camera.position.z = 5;

const animate = () => {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
};
animate();
