"use client";

import {
  type ReactNode,
  type RefObject,
  useEffect,
  useState,
  useSyncExternalStore,
} from "react";
import styles from "./diagram.module.css";

export function usePrefersReducedMotion() {
  return useSyncExternalStore(
    (onStoreChange) => {
      const query = window.matchMedia("(prefers-reduced-motion: reduce)");
      query.addEventListener("change", onStoreChange);
      return () => query.removeEventListener("change", onStoreChange);
    },
    () => window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    () => true,
  );
}

export function useDiagramVisibility<T extends Element>(
  ref: RefObject<T | null>,
) {
  const [inView, setInView] = useState(false);
  const [pageVisible, setPageVisible] = useState(false);

  useEffect(() => {
    const updatePageVisibility = () => setPageVisible(!document.hidden);
    updatePageVisibility();
    document.addEventListener("visibilitychange", updatePageVisibility);
    return () => document.removeEventListener("visibilitychange", updatePageVisibility);
  }, []);

  useEffect(() => {
    const node = ref.current;
    if (!node) return;

    if (typeof IntersectionObserver === "undefined") {
      const frame = window.requestAnimationFrame(() => setInView(true));
      return () => window.cancelAnimationFrame(frame);
    }

    const observer = new IntersectionObserver(
      ([entry]) => setInView(entry.isIntersecting),
      { rootMargin: "120px 0px", threshold: 0.05 },
    );

    observer.observe(node);
    return () => observer.disconnect();
  }, [ref]);

  return inView && pageVisible;
}

type AriaCurrent = "page" | "step" | "location" | "date" | "time" | true;

export function ControlButton({
  children,
  onClick,
  active,
  pressed,
  current,
  disabled,
  label,
}: {
  children: ReactNode;
  onClick: () => void;
  active?: boolean;
  pressed?: boolean;
  current?: AriaCurrent;
  disabled?: boolean;
  label?: string;
}) {
  return (
    <button
      type="button"
      className={styles.controlButton}
      data-active={active || pressed || current ? "true" : undefined}
      aria-pressed={pressed}
      aria-current={current}
      aria-label={label}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
